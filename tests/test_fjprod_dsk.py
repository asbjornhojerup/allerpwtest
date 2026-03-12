"""Familiejournal production tests - desktop"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_desktop(page: Page):
    """Configure page for desktop viewport."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


def test_accept_all_cookies(page_desktop: Page):
    """Test accepting all cookies."""
    page_desktop.goto("https://familiejournal.dk/")
    page_desktop.get_by_role("button", name="Tillad alle").click()


def test_open_menu_item_go_to_category(page_desktop: Page):
    """Test opening menu item and navigating to category."""
    page_desktop.goto("https://familiejournal.dk/")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.get_by_role("link", name="Livshistorier").first.hover()
    page_desktop.get_by_role("link", name="Artikler", exact=True).click()
    expect(page_desktop.get_by_role("heading", name="Artikler")).to_be_visible()


def test_load_more_on_category_page(page_desktop: Page):
    """Test load more functionality on category page."""
    page_desktop.goto("https://familiejournal.dk/livshistorier")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_desktop: Page):
    """Test opening article from category page."""
    page_desktop.goto("https://familiejournal.dk/livshistorier")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.locator('//div[@class="w-full whitespace-normal left-0 bottom-0 relative -mt-10 lg:-mt-10 lg:ml-0"]').first.click()
    expect(page_desktop.locator('//div[@class="uppercase font-bold text-red-400 text-14 mb-10 tracking-[1.4px] grid"]')).to_be_visible()


def test_newsletter_signup(page_desktop: Page):
    """Test newsletter signup form."""
    page_desktop.goto("https://familiejournal.dk/nyhedsbrev")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.locator('//input[@id="edit-email"]').fill("jjk@mailinator.com")
    page_desktop.locator('//input[@id="edit-first-name"]').fill("Jens")
    page_desktop.locator('//input[@id="edit-last-name"]').fill("Jensen")
    page_desktop.locator('//input[@id="edit-phone-number"]').fill("40704070")
    page_desktop.locator('//input[@id="edit-zip-code"]').fill("4070")
    page_desktop.locator('//input[@id="edit-agree"]').click()
    page_desktop.locator('//button[@type="submit"]').click()


def test_direct_link_to_article(page_desktop: Page):
    """Test accessing article via direct link."""
    page_desktop.goto(
        "https://www.familiejournal.dk/livshistorier/artikler/til-konfirmationsforberedelse-fandt-alfred-ro-elsker-gaa-i-kirke"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()


def test_video_player_total_consent(page_desktop: Page):
    """Test video player with all cookies allowed."""
    page_desktop.goto(
        "https://www.familiejournal.dk/livshistorier/artikler/til-konfirmationsforberedelse-fandt-alfred-ro-elsker-gaa-i-kirke"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_desktop: Page):
    """Test video player with necessary cookies only."""
    page_desktop.goto(
        "https://www.familiejournal.dk/livshistorier/artikler/til-konfirmationsforberedelse-fandt-alfred-ro-elsker-gaa-i-kirke"
    )
    page_desktop.get_by_role("button", name="Reject all").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_load_more_category_change_consent(page_desktop: Page):
    """Test load more with consent change."""
    page_desktop.goto("https://familiejournal.dk/livshistorier")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.get_by_role("button", name="Hent flere").click()
    page_desktop.get_by_role("button", name="Administrer samtykke").click()
    page_desktop.get_by_role("button", name="Reject all").click()
    page_desktop.get_by_role("button", name="Hent flere").click()


def test_ad_placements_on_frontpage(page_desktop: Page):
    """Test ad placements on frontpage."""
    page_desktop.goto("https://familiejournal.dk?debugAds=true")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()
    page_desktop.evaluate("window.scrollBy(500, 2500)")
    expect(page_desktop.locator("#responsive_2-1")).to_be_visible()


def test_ad_placements_on_article(page_desktop: Page):
    """Test ad placements on article page."""
    page_desktop.goto(
        "https://www.familiejournal.dk/livshistorier/artikler/til-konfirmationsforberedelse-fandt-alfred-ro-elsker-gaa-i-kirke"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.evaluate("window.scrollBy(0, 500)")
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()
    page_desktop.evaluate("window.scrollBy(500, 2500)")
    expect(page_desktop.locator("#intext_ad_3-1")).to_be_visible(timeout=10000)
