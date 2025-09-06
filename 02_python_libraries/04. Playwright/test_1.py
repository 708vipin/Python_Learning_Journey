# test_simple_form_demo.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])  # run in parallel
def test_simple_form_demo(browser_name, playwright):
    # Launch browser with tracing, video, console + network logging
    browser = getattr(playwright, browser_name).launch(
        headless=False,  # change to True in CI
    )

    context = browser.new_context(
        record_video_dir="videos/",
        record_har_path=f"har_logs/{browser_name}.har",  # network logs
    )

    page = context.new_page()

    # Collect console logs
    page.on("console", lambda msg: print(f"[{browser_name} console] {msg.type}: {msg.text}"))

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Step 1: Open playground
    page.goto("https://www.lambdatest.com/selenium-playground")

    # Step 2: Click "Simple Form Demo"
    page.click("text=Simple Form Demo")

    # Step 3: Validate URL
    assert "simple-form-demo" in page.url

    # Step 4: Variable with string
    test_message = "Welcome to LambdaTest"

    # Step 5: Enter message
    page.fill("#user-message", test_message)

    # Step 6: Click button
    page.click("text=Get Checked Value")

    # Step 7: Validate output
    output_text = page.text_content("#message")
    assert test_message in output_text

    # Stop tracing and save
    context.tracing.stop(path=f"traces/{browser_name}_trace.zip")

    context.close()
    browser.close()


