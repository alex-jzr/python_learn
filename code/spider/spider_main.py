from fetch_and_save_page import fetch_and_save_page
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.panel = wx.Panel(self)  # 创建一个面板
        self.url_text = wx.TextCtrl(self.panel, value="请输入URL", pos=(10, 10), size=(300, 25))  # 输入框
        self.button = wx.Button(self.panel, label="抓取页面", pos=(10, 50))  # 按钮
        self.result_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE, pos=(10, 90), size=(400, 200))  # 用于显示结果的文本框

        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)  # 按钮绑定事件

    def on_button_click(self, event):
        url = self.url_text.GetValue()  # 获取用户在输入框中输入的URL
        self.result_text.SetValue(f"正在抓取 {url}...\n")  # 在结果框显示正在抓取的提示
        try:
            
            # 在这里调用你的爬虫函数
            
            fetch_and_save_page(url)
            self.result_text.AppendText(f"页面已保存到 E:\\code\\spider\\page_content.txt\n")  # 显示成功信息
        except Exception as e:
            self.result_text.AppendText(f"发生错误: {e}\n")  # 显示错误信息


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="简单爬虫", size=(500, 350))  # 创建窗口
        self.frame.Show()  # 显示窗口
        return True


if __name__ == "__main__":
    app = MyApp()  # 启动应用
    app.MainLoop()
