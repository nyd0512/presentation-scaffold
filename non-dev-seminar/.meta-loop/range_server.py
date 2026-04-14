#!/usr/bin/env python3
"""HTTP server with Range request support for video streaming QA."""
import http.server
import os
import socketserver
import sys
from http import HTTPStatus

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8900


class RangeHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()
        try:
            f = open(path, "rb")
        except OSError:
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return None
        try:
            fs = os.fstat(f.fileno())
            size = fs.st_size
            rng = self.headers.get("Range")
            ctype = self.guess_type(path)

            if rng and rng.startswith("bytes="):
                try:
                    start_s, end_s = rng[6:].split("-", 1)
                    start = int(start_s) if start_s else 0
                    end = int(end_s) if end_s else size - 1
                    if start >= size or end >= size or start > end:
                        self.send_error(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE)
                        f.close()
                        return None
                    length = end - start + 1
                    self.send_response(HTTPStatus.PARTIAL_CONTENT)
                    self.send_header("Content-Type", ctype)
                    self.send_header("Accept-Ranges", "bytes")
                    self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
                    self.send_header("Content-Length", str(length))
                    self.end_headers()
                    f.seek(start)
                    # return a bounded file
                    return _Bounded(f, length)
                except ValueError:
                    pass

            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", ctype)
            self.send_header("Accept-Ranges", "bytes")
            self.send_header("Content-Length", str(size))
            self.end_headers()
            return f
        except Exception:
            f.close()
            raise


class _Bounded:
    def __init__(self, f, n):
        self._f = f
        self._n = n

    def read(self, size=-1):
        if self._n <= 0:
            return b""
        if size < 0 or size > self._n:
            size = self._n
        data = self._f.read(size)
        self._n -= len(data)
        return data

    def close(self):
        self._f.close()


class ReusableTCP(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with ReusableTCP(("", PORT), RangeHandler) as httpd:
        print(f"Range server on :{PORT}", flush=True)
        httpd.serve_forever()
