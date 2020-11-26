from guietta import _, Gui, Quit
#from PySide2 import QtWidgets (sim izskatas vajag py3.8.1)

# pip install guietta
# pip install PySide2
# pip install PyQt5

# https://guietta.readthedocs.io/en/stable/tutorial.html

gui = Gui(

  [  'Enter numbers:', '__a__'  , '+' , '__b__',  ['Calculate'] ],
  [  'Result:  -->'  , 'result' ,  _  ,    _   ,       _        ],
  [  _               ,    _     ,  _  ,    _   ,      Quit      ],
  [  ['acc.png']     ,    _     ,  _  ,    _   ,      _         ]

)

with gui.Calculate:
    gui.result = float(gui.a) + float(gui.b)

gui.run()