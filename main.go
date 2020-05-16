package main

import (
	"os"

	"fyne.io/fyne"
	"fyne.io/fyne/app"
	"fyne.io/fyne/widget"
)

func main() {
	err := os.Setenv("FYNE_FONT", "fonts/YaHei.Consolas.1.11b.ttf")
	if err != nil {
		return
	}
	defer os.Unsetenv("FYNE_FONT")

	myApp := app.New()

	w := myApp.NewWindow("你好 Hello World!")
	w.SetContent(widget.NewLabel("你好 Hello World!"))
	w.Resize(fyne.Size{500,400})

	w.ShowAndRun()
}
