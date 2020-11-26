from guietta import _, Gui, Quit


gui = Gui(

  [  'Enter numbers:', '__a__'  , '+' , '__b__',  ['Calculate'] ],
  [  'Result:  -->'  , 'result' ,  _  ,    _   ,       _        ],
  [  _               ,    _     ,  _  ,    _   ,      Quit      ],
  [  ['acc.png']     ,    _     ,  _  ,    _   ,      _         ]

)

with gui.Calculate:
    gui.result = float(gui.a) + float(gui.b)

gui.run()