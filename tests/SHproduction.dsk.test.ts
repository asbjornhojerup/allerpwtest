import { test, expect } from '@playwright/test';
test.use({ viewport: { width: 1920, height: 1080 } });

test('test accept all cookies', async ({ page }) => {
    await page.goto('https://seoghoer.dk/');
    await page.getByRole('button', { name: 'Allow all cookies' }).click();
  });

test('test open menu, go to category', async ({ page }) => {
  await page.goto('https://seoghoer.dk/');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Menu' }).click();
  await page.getByRole('link', { name: 'Kendte', exact: true }).click();
});

test('test go to frontpage by clicking logo', async ({ page }) => {
  await page.goto('https://seoghoer.dk/kendte');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//div[contains(@class ,"-mb-5 mr-auto transition-dimensions duration-500 h-80")]').click();
});

test('test load more  on category page', async ({ page }) => {
  await page.goto('https://seoghoer.dk/kendte');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test open article on category page', async ({ page }) => {
  await page.goto('https://seoghoer.dk/kongelige');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//div[contains(@class ,"relative mr-10 md:mr-0 md:mb-10 bg-grey-300 aspect-video w-full lg:min-w-[160px]")]').hover();
  await page.locator('//div[contains(@class ,"relative mr-10 md:mr-0 md:mb-10 bg-grey-300 aspect-video w-full lg:min-w-[160px]")]').click();
    await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="text-20 leading-26 font-bold mb-20"]')).toBeVisible();
});


test('test newsletter sign-up', async ({ page }) => {
  await page.goto('https://seoghoer.dk/nyhedsbrev');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//input[@id="email"]').fill('jjk@mailinator.com');
  await page.locator('//input[@id="firstname"]').fill('Jens');
  await page.locator('//input[@id="postal"]').fill('4070');
  await page.locator('//input[@id="terms"]').click();
  await page.locator('//button[@type="submit"]').click();
});

test('direct link to article', async ({ page }) => {
  await page.goto('https://seoghoer.dk/kongelige/glenn-bech-afsloerer-kronprins-christian-faldt-i-soevn-under-foredrag');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
});

//tests if jw player is loaded after marketing consent is given
test('test video player, total consent', async ({ page }) => {
  await page.goto('https://seoghoer.dk/kongelige/glenn-bech-afsloerer-kronprins-christian-faldt-i-soevn-under-foredrag');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

//tests if jw player is shown on use of necessary consent
test('test video player, necessary consent', async ({ page }) => {
  await page.goto('https://seoghoer.dk/kongelige/glenn-bech-afsloerer-kronprins-christian-faldt-i-soevn-under-foredrag');
  await page.getByRole('button', { name: 'Use necessary cookies only' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

test('test load more  on category , change to necessary cookies, load more again', async ({ page }) => {
  await page.goto('https://seoghoer.dk/kendte');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
  await page.getByRole('button', { name: 'Administrer samtykke' }).click();
  await page.getByRole('button', { name: 'Use Necessary cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test ad placements on frontpage', async ({ page }) => {
  await page.goto('https://seoghoer.dk?debugAds=true');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});

test('test ad placements on article', async ({ page }) => {
  await page.goto('https://seoghoer.dk/kendte/midt-i-sygdomschok-kendte-sender-kaerlighed-til-melvin-kakooza?debugAds=true');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});
