import { test, expect } from '@playwright/test';
test.use({viewport:{width:390,height:844}});

test('test accept all cookies', async ({ page }) => {
    await page.goto('https://isabellas.dk/');
    await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  });

test('test open menu item, go to category', async ({ page }) => {
  await page.goto('https://isabellas.dk/');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await page.getByRole('button', { name: 'Menu' }).click();
  await page.getByRole('button', { name: 'Udfold menu', exact: true }).first().click();
  await page.getByRole('link', { name: 'Havetips', exact: true }).first().click();
  {timeout: 30000}
  await expect(page.getByRole('heading', { name: 'Havetips', exact: true})).toBeVisible();
});


test('test load more  on category page', async ({ page }) => {
  await page.goto('https://isabellas.dk/haven');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test open article on category page', async ({ page }) => {
  await page.goto('https://isabellas.dk/haven');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await page.locator('//*[@class="max-w-full pt-30 px-30 pb-70 md:pt-20 md:pb-75 flex-grow flex flex-col"]').first().click();
  await expect(page.locator('//div[@class="font-bold tracking-0-6 text-12 leading-18 mb-10 text-center uppercase"]')).toBeVisible();
});


//test('test newsletter sign-up', async ({ page }) => {
  //await page.goto('https://isabellas.dk/nyhedsbrev');
  //await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  //await page.locator('//input[@id="E-mail *"]').fill('jjk@mailinator.com');
  //await page.locator('//input[@id="fornavn"]').fill('Jens');
  //await page.locator('//input[@id="edit-last-name"]').fill('Jensen');
  //await page.locator('//input[@id="edit-phone-number"]').fill('40704070');
  //await page.locator('//input[@id="edit-zip-code"]').fill('4070');
  //await page.locator('//input[@id="edit-agree"]').click();
  //await page.locator('//button[@type="submit"]').click();
//});

test('direct link to article', async ({ page }) => {
  await page.goto('https://isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
});

//tests if jw player is loaded after marketing consent is given
test('test video player, total consent', async ({ page }) => {
  await page.goto('https://isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 9000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

//tests if jw player is shown on use of necessary consent
test('test video player, necessary consent', async ({ page }) => {
  await page.goto('https://isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker');
  await page.getByRole('button', { name: 'Kun nødvendige cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 9000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

test('test ad placements on frontpage', async ({ page }) => {
  await page.goto('https://isabellas.dk');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});

test('test ad placements on article', async ({ page }) => {
  await page.goto('https://isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});
