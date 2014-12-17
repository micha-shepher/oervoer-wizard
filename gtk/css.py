#!/usr/bin/python
from gi.repository import Gtk, Gdk

win = Gtk.Window()
win.set_name('MyWindow')

# The Button
button = Gtk.Button("Click Me")
win.add(button)


win.connect("delete-event", Gtk.main_quit)

style_provider = Gtk.CssProvider()

css = """
#MyWindow {
    background-color: #F00;
}
"""

style_provider.load_from_data(css)

Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), 
    style_provider,     
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

win.show_all()
Gtk.main()
