import { test, expect } from '@playwright/test';
test.use({ viewport: { width: 1920, height: 1080 } });

test('test accept all cookies', async ({ page }) => {
    await page.goto('https://udeoghjemme.dk/');
    await page.getByRole('button', { name: 'Allow all cookies' }).click();
  });

test('test open menu item, go to category', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('#header-main').getByRole('link', { name: 'Skæbner' }).hover();
  await page.getByRole('link', { name: 'Når livet gør ondt', exact: true }).first().click();
  {timeout: 30000}
  await expect(page.getByRole('heading', { name: 'Når livet gør ondt' })).toBeVisible();
});


test('test load more  on category page', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/skaebner');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test open article on category page', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/skaebner');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//div[@class="min-w-[fit-content]"]').first().click();
  await expect(page.locator('//div[@class="mb-30 md:mb-20 mx-20 text-20 leading-26 text-black font-light font-condensed lg:text-24 lg:leading-30"]')).toBeVisible();
});


test('test newsletter sign-up', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/nyhedsbrev');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//input[@id="edit-email"]').fill('jjk@mailinator.com');
  await page.locator('//input[@id="edit-first-name"]').fill('Jens');
  await page.locator('//input[@id="edit-last-name"]').fill('Jensen');
  await page.locator('//input[@id="edit-phone-number"]').fill('40704070');
  await page.locator('//input[@id="edit-zip-code"]').fill('4070');
  await page.locator('//input[@id="edit-agree"]').click();
  await page.locator('//button[@type="submit"]').click();
});

test('direct link to article', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/reality/love-island/love-island-deltageren-jamie-eschen-skal-i-faengsel-igen-hun-kunne-ikke-faa');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
});

//tests if jw player is loaded after marketing consent is given
test('test video player, total consent', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/skaebner/naar-livet-goer-ondt/marlene-fik-sin-elskede-john-viet-paa-hans-doedsleje');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

//tests if jw player is shown on use of necessary consent
test('test video player, necessary consent', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/skaebner/naar-livet-goer-ondt/marlene-fik-sin-elskede-john-viet-paa-hans-doedsleje');
  await page.getByRole('button', { name: 'Use necessary cookies only' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

test('test load more  on category , change to necessary cookies, load more again', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/skaebner');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
  await page.getByRole('button', { name: 'Administrer samtykke' }).click();
  await page.getByRole('button', { name: 'Use Necessary cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test ad placements on frontpage', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});

test('test ad placements on article', async ({ page }) => {
  await page.goto('https://udeoghjemme.dk/skaebner/naar-livet-goer-ondt/123-omkom-da-olieplatform-kaentrede-anders-sprang-i-havet-og');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});

