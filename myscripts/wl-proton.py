import sys
p = sys.argv[1]
s = open(p).read()
a = '        self.check_environment("PROTON_HIDE_APU", "hideapu")\n'
assert s.count(a) == 1
b = a + "".join([
    '        self.check_environment("PROTON_ENABLE_WAYLAND", "enablewayland")\n',
    '        if "enablewayland" in self.compat_config and "WAYLAND_DISPLAY" in self.env:\n',
    '            self.dlloverrides["winex11.drv"] = "d"\n',
    '            self.dlloverrides["winewayland.drv"] = "b"\n',
])
open(p, "w").write(s.replace(a, b))