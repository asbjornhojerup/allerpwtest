"""Seoghoer staging tests - mobile"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_mobile(page: Page):
    """Configure page for mobile viewport."""
    page.set_viewport_size({"width": 390, "height": 844})
    yield page


def test_accept_all_cookies(page_mobile: Page):
    """Test accepting all cookies."""
    page_mobile.goto("https://frontend-stage.seoghoer.dk/")
    page_mobile.get_by_role("button", name="Tillad alle").click()


def test_open_menu_go_to_category(page_mobile: Page):
    """Test opening menu and navigating to category."""
    page_mobile.goto("https://frontend-stage.seoghoer.dk/")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_label("menu").click()
    page_mobile.get_by_role("link", name="Kendte").click()


def test_go_to_frontpage_by_clicking_logo(page_mobile: Page):
    """Test returning to frontpage via logo."""
    page_mobile.goto("https://frontend-stage.seoghoer.dk/kendte")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.locator('//div[contains(@class ,"-mb-5 mr-auto transition-dimensions duration-500 h-80")]').click()


def test_load_more_on_category_page(page_mobile: Page):
    """Test load more functionality on category page."""
    page_mobile.goto("https://frontend-stage.seoghoer.dk/kendte")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_mobile: Page):
    """Test opening article from category page."""
    page_mobile.goto("https://frontend-stage.seoghoer.dk/kendte")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.locator('//div[contains(@class ,"max-w-full text-center bg-grey-200 lg:bg-white px-30 md:px-0 py-8 md:py-0 md:text-left")]').hover()
    page_mobile.locator('//div[contains(@class ,"max-w-full text-center bg-grey-200 lg:bg-white px-30 md:px-0 py-8 md:py-0 md:text-left")]').click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="text-20 leading-26 font-bold mb-20"]')).to_be_visible()


def test_newsletter_signup(page_mobile: Page):
    """Test newsletter signup form."""
    page_mobile.goto("https://frontend-stage.seoghoer.dk/nyhedsbrev")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.locator('//input[@placeholder="e-mail"]').fill("jjk@mailinator.com")
    page_mobile.locator('//input[@id="fornavn"]').fill("Jens")
    page_mobile.locator('//input[@id="efternavn"]').fill("jakob")
    page_mobile.locator('//input[@id="postal"]').fill("4070")
    page_mobile.locator('//input[@id="terms"]').click()
    page_mobile.locator('//button[@type="submit"]').click()


def test_direct_link_to_article(page_mobile: Page):
    """Test accessing article via direct link."""
    page_mobile.goto(
        "https://frontend-stage.seoghoer.dk/reality/love-island/love-island-deltageren-jamie-eschen-skal-i-faengsel-igen-hun-kunne-ikke-faa"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()


def test_video_player_total_consent(page_mobile: Page):
    """Test video player with all cookies allowed."""
    page_mobile.goto(
        "https://frontend-stage.seoghoer.dk/reality/paradise-hotel/voldsom-video-nadja-hansen-i-dramatisk-ormeulykke-paa-paradise-hotel"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_mobile: Page):
    """Test video player with necessary cookies only."""
    page_mobile.goto(
        "https://frontend-stage.seoghoer.dk/reality/paradise-hotel/voldsom-video-nadja-hansen-i-dramatisk-ormeulykke-paa-paradise-hotel"
    )
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_load_more_category_change_consent(page_mobile: Page):
    """Test load more with consent change."""
    page_mobile.goto("https://frontend-stage.seoghoer.dk/kendte")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Hent flere").click()
    page_mobile.get_by_role("button", name="Administrer samtykke").click()
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_ad_placements_on_frontpage(page_mobile: Page):
    """Test ad placements on frontpage."""
    page_mobile.goto("https://frontend-stage.seoghoer.dk")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_mobile: Page):
    """Test ad placements on article page."""
    page_mobile.goto(
        "https://frontend-stage.seoghoer.dk/reality/love-island/love-island-deltageren-jamie-eschen-skal-i-faengsel-igen-hun-kunne-ikke-faa?debugAds=true"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()
