#!/usr/bin/env python

import os
import web

from config import STORAGE_PATH, DEBUG

urls = (
    '/', 'Index',
    '/id/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', 'IdGenerator'
)


class Index(object):

    def GET(self):
        return 'Welcome to the build id generator!'


class IdGenerator(object):

    def GET(self, uuid):
        uuid = str(uuid)
        id_storage_path = os.path.join(STORAGE_PATH, "%s.id" % uuid)

        if os.path.exists(id_storage_path):
            f = file(id_storage_path, "r+")
            count = f.read()
            if count == '':
                count = 1
            else:
                count = int(count)
                count += 1
        else:
            f = file(id_storage_path, "w")
            count = 1
        f.seek(0)
        f.write(str(count))
        f.close()
        return str(count)


if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = DEBUG

    app.run()
