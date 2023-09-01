from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindow:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(
                driver, "https://demoqa.com/browser-windows"
            )
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened("window")
            assert (
                text_result == "This is a sample page"
            ), "the new tab/window has not opened or an incorrect tab has opened"
