package main

import (
	"fyne.io/fyne/app"
	"fyne.io/fyne/widget"
)

func main() {
	myApp := app.New()

	w := myApp.NewWindow("Hello")
	w.SetContent(widget.NewLabel("Hello Fyne!"))

	w.ShowAndRun()
}
