import { ClickSocialWebPage } from './app.po';

describe('click-social-web App', () => {
  let page: ClickSocialWebPage;

  beforeEach(() => {
    page = new ClickSocialWebPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
