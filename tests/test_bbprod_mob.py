"""Billedbladet production tests - mobile"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_mobile(page: Page):
    """Configure page for mobile viewport."""
    page.set_viewport_size({"width": 390, "height": 844})
    yield page


def test_open_menu_go_to_category(page_mobile: Page):
    """Test opening menu and navigating to category."""
    page_mobile.goto("https://billedbladet.dk/")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_label("Åben menu").click()
    page_mobile.get_by_role("link", name="Kendte", exact=True).click()


def test_go_to_frontpage_by_clicking_logo(page_mobile: Page):
    """Test returning to frontpage via logo."""
    page_mobile.goto("https://billedbladet.dk/kendte")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("link", name="Gå til forsiden").click()


def test_load_more_on_category_page(page_mobile: Page):
    """Test load more functionality on category page."""
    page_mobile.goto("https://billedbladet.dk/kendte")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_mobile: Page):
    """Test opening article from category page."""
    page_mobile.goto("https://billedbladet.dk/kendte")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.locator('//*[@class="rounded-t-10 bg-gray-100 bg-opacity-50"]').click()
    expect(page_mobile.get_by_role("heading", name="Mest Læste")).to_be_visible()


def test_newsletter_signup(page_mobile: Page):
    """Test newsletter signup form."""
    page_mobile.goto("https://billedbladet.dk/nyhedsbrev")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.locator('//input[@id="email"]').fill("jjk@mailinator.com")
    page_mobile.locator('//input[@id="firstname"]').fill("Jens")
    page_mobile.locator('//input[@id="postalcode"]').fill("4070")
    page_mobile.locator('//input[@id="terms"]').click()
    page_mobile.locator('//button[@type="submit"]').click()


def test_direct_link_to_article(page_mobile: Page):
    """Test accessing article via direct link."""
    page_mobile.goto(
        "https://billedbladet.dk/nostalgi/husker-du-da-benedikte-og-anne-marie-forstyrrede-fars-nytaarstale"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()


def test_video_player_total_consent(page_mobile: Page):
    """Test video player with all cookies allowed."""
    page_mobile.goto(
        "https://www.billedbladet.dk/kongelige/danmark/prinsesse-josephine-og-prins-vincents-glamouroese-look-glimtende-stene-og-james"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_mobile: Page):
    """Test video player with necessary cookies only."""
    page_mobile.goto(
        "https://www.billedbladet.dk/kongelige/danmark/prinsesse-josephine-og-prins-vincents-glamouroese-look-glimtende-stene-og-james"
    )
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_load_more_category_change_consent(page_mobile: Page):
    """Test load more with consent change."""
    page_mobile.goto("https://billedbladet.dk/kendte")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Hent flere").click()
    page_mobile.get_by_role("button", name="Administrer samtykke").click()
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_ad_placements_on_frontpage(page_mobile: Page):
    """Test ad placements on frontpage."""
    page_mobile.goto("https://billedbladet.dk")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_mobile: Page):
    """Test ad placements on article page."""
    page_mobile.goto("https://billedbladet.dk/kongelige/danmark/se-videoen-her-ankommer-kongeparret-til-nytaarskur")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()
