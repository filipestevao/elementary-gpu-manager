#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class processDialog(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_border_width(10)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        label = Gtk.Label("Processing. Please wait.")
        self.vbox.add(label)

        spinner = Gtk.Spinner()
        spinner.set_margin_top(5)
        self.vbox.add(spinner)
        spinner.start()

if __name__ == "__main__":
    win = processDialog()
    win.set_decorated(False)
    win.set_resizable(False)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
