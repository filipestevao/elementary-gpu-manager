#!/usr/bin/python3

import subprocess
import multiprocessing

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class MyApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GPU Manager")
        self.set_border_width(10)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)
        self.vbox.set_spacing(5)
        
        label = Gtk.Label()
        label.set_markup("<b>Power Profile</b>")
        self.vbox.pack_start(label, True, True, 0)
        
        self.radioButtonPower()
        
        label = Gtk.Label()
        label.set_markup("<b>GPU Manager</b>")
        label.set_margin_top(15)
        self.vbox.pack_start(label, True, True, 0)
        
        self.radioButtonGPU()
        
        button = Gtk.Button.new_with_label("Apply (requires restart)")
        button.connect("clicked", self.on_button_clicked)
        self.vbox.pack_start(button, True, True, 0)

    def on_button_clicked(self, button):
        p1 = multiprocessing.Process(target=self.apply_graphics)
        p2 = multiprocessing.Process(target=self.call_loading)
        p1.start()
        p2.start()
       
        while True:
            if not p1.is_alive():
                subprocess.run(['pkill', 'loading-win.py'])
                break

        self.restart_question()
    
    def apply_graphics(self):
        subprocess.run(['system76-power', 'graphics', self.switchGPU])

    def call_loading(self):
        subprocess.run(['./loading-win.py'])
        
    def radioButtonPower(self):
        RBperformance = Gtk.RadioButton.new_with_label_from_widget(None, "High Performance")
        RBbalanced = Gtk.RadioButton.new_with_label_from_widget(RBperformance, "Balanced")
        RBbattery = Gtk.RadioButton.new_with_label_from_widget(RBperformance, "Battery Life")
        
        getProfile = subprocess.getoutput('system76-power profile')
        if 'Performance' in getProfile:
            RBperformance.set_active(True)
        elif 'Balanced' in getProfile:
            RBbalanced.set_active(True)
        elif 'Battery' in getProfile:
            RBbattery.set_active(True)
        
        # RBperformance
        RBperformance.connect("toggled", self.on_button_toggled, "performance")
        self.vbox.pack_start(RBperformance, False, False, 0)
        
        # RBbalanced
        RBbalanced.connect("toggled", self.on_button_toggled, "balanced")
        self.vbox.pack_start(RBbalanced, False, False, 0)
        
        # RBbattery
        RBbattery.connect("toggled", self.on_button_toggled, "battery")
        self.vbox.pack_start(RBbattery, False, False, 0)
    
    def on_button_toggled(self, button, name):
        if button.get_active():
            subprocess.run(['system76-power', 'profile', name])
    
    def radioButtonGPU(self):
        RBnvidia = Gtk.RadioButton.new_with_label_from_widget(None, "NVIDIA Graphics")
        RBintel = Gtk.RadioButton.new_with_label_from_widget(RBnvidia, "Intel Graphics")
        
        getGPU = subprocess.getoutput('system76-power graphics')
        if 'nvidia' in getGPU:
            RBnvidia.set_active(True)
        elif 'intel' in getGPU:
            RBintel.set_active(True)
        
        # RBnvidia
        RBnvidia.connect("toggled", self.setGPU, "nvidia")
        self.vbox.pack_start(RBnvidia, False, False, 0)
        
        # RBintel
        RBintel.connect("toggled", self.setGPU, "intel")
        self.vbox.pack_start(RBintel, False, False, 0)
    
    def setGPU(self, button, name):
        if button.get_active():
            self.switchGPU = name
    
    def restart_question(self):
        dialog = Gtk.MessageDialog(
            self,
            0,
            Gtk.MessageType.QUESTION,
            Gtk.ButtonsType.YES_NO,
            "Restart now?",
        )
        dialog.format_secondary_text(
            "Do you want to restart now to apply the changes?"
        )
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            subprocess.run(['reboot'])

        dialog.destroy()


if __name__ == "__main__":
    win = MyApp()
    win.set_resizable(False)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

