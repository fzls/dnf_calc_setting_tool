package main

import (
	"fmt"
	"os"

	"fyne.io/fyne"
	"fyne.io/fyne/app"
	"fyne.io/fyne/widget"
	"go.uber.org/zap"
)

var logger *zap.SugaredLogger

func main() {
	var err error
	logger, err = initLogger()
	if err != nil {
		panic(fmt.Sprintf("init logger failed, err=%v", err))
	}
	defer logger.Sync()

	// 设置fyne中文字体环境变量，使得中文字体不乱码
	err = os.Setenv("FYNE_FONT", "fonts/YaHei.Consolas.1.11b.ttf")
	if err != nil {
		logger.Errorf("设置中文字体出错=%v", err)
		return
	}

	myApp := app.New()

	w := myApp.NewWindow("你好 Hello World!")
	w.SetContent(widget.NewLabel("你好 Hello World!"))
	w.Resize(fyne.Size{500, 400})

	logger.Info("配置工具启动成功")

	w.ShowAndRun()
}
