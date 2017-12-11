import re

iso8601pattern = re.compile("^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+.)?(\d+S)?)?$")

iso8601pattern.match(namespace.lock_duration)
