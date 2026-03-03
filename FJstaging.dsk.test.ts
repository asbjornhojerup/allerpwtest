import { test, expect } from '@playwright/test';
test.use({ viewport: { width: 1920, height: 1080 } });

test('test accept all cookies', async ({ page }) => {
    await page.goto('https://frontend-stage.familiejournal.dk/');
    await page.getByRole('button', { name: 'Allow all cookies' }).click();
  });

test('test open menu item, go to category', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk/');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('link', { name: 'Livshistorier' }).first().hover();
  await page.getByRole('link', { name: 'Artikler', exact: true }).click();
  {timeout: 30000}
  await expect(page.getByRole('heading', { name: 'Artikler' })).toBeVisible();
});


test('test load more  on category page', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk/livshistorier');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test open article on category page', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk/livshistorier');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//div[@class="w-full whitespace-normal left-0 bottom-0 relative -mt-10 lg:-mt-10 lg:ml-0"]').first().click();
  await expect(page.locator('//div[@class="uppercase font-bold text-red-400 text-14 mb-10 tracking-[1.4px] grid"]')).toBeVisible();
});


test('test newsletter sign-up', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk/nyhedsbrev');
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
  await page.goto('https://frontend-stage.familiejournal.dk/livshistorier/artikler/til-konfirmationsforberedelse-fandt-alfred-ro-elsker-gaa-i-kirke');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
});

//tests if jw player is loaded after marketing consent is given
test('test video player, total consent', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk/livshistorier/artikler/til-konfirmationsforberedelse-fandt-alfred-ro-elsker-gaa-i-kirke');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

//tests if jw player is shown on use of necessary consent
test('test video player, necessary consent', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk/livshistorier/artikler/til-konfirmationsforberedelse-fandt-alfred-ro-elsker-gaa-i-kirke');
  await page.getByRole('button', { name: 'Reject all' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

test('test load more  on category , change to necessary cookies, load more again', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk/livshistorier');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
  await page.getByRole('button', { name: 'Administrer samtykke' }).click();
  await page.getByRole('button', { name: 'Reject all' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test ad placements on frontpage', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk?debugAds=true');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
        await page.evaluate(() => { 
  window.scrollBy(0, 5000);
});
  await expect(page.locator('#responsive_2-1')).toBeVisible();
});

test('test ad placements on article', async ({ page }) => {
  await page.goto('https://frontend-stage.familiejournal.dk/livshistorier/artikler/til-konfirmationsforberedelse-fandt-alfred-ro-elsker-gaa-i-kirke');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
          await page.evaluate(() => { 
  window.scrollBy(0, 500);
});
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});
