import pytest
from playwright.sync_api import sync_playwright
import time

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

def test_play_video_and_close(browser):
    page = browser.new_page()

    # Mở trang YouTube
    page.goto('https://www.youtube.com')
    page.fill('input[name="search_query"]', 'Sơn Tùng M-TP')
    page.click('button[id="search-icon-legacy"]')
    page.wait_for_selector('a[id="video-title"]')

    # Click vào video đầu tiên
    page.click('a[id="video-title"]')

    # Chờ cho video được tải
    page.wait_for_selector('button[id="button"]')

    # Xem video trong 1 phút
    time.sleep(60)

    # Kiểm tra xem video đã được phát thành công chưa
    assert page.evaluate('() => document.querySelector("video").paused') == False

    # Đóng trang
    page.close()
