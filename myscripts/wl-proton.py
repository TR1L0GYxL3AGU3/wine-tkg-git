import sys
p = sys.argv[1]
s = open(p).read()
a = '        self.check_environment("PROTON_HIDE_APU", "hideapu")\n'
assert s.count(a) == 1
b = a + "".join([
    '        self.check_environment("PROTON_ENABLE_WAYLAND", "wayland")\n',
    '        self.check_environment("PROTON_USE_WAYLAND", "wayland")\n',
    '        if "wayland" in self.compat_config and "WAYLAND_DISPLAY" in self.env:\n',
    '            if "PROTON_WAYLAND_MONITOR" in self.env:\n',
    '                self.env["WAYLANDDRV_PRIMARY_MONITOR"] = self.env["PROTON_WAYLAND_MONITOR"]\n',
    '            self.env["WINE_GRAPHICS_DRIVER"] = "wayland"\n',
    '            self.dlloverrides["winewayland.drv"] = "b"\n',
    '            self.env["WINE_USE_EGL"] = "1"\n',
    '            self.env["WINE_DISABLE_FULLSCREEN_HACK"] = "1"\n',
    '            self.env.setdefault("WINE_MOVE_HACK", "1")\n',
    '            self.env["PROTON_USE_XALIA"] = "0"\n',
    '            self.env.setdefault("XLOCALEDIR", g_proton.dist_dir + "share/X11/locale")\n',
])
open(p, "w").write(s.replace(a, b))