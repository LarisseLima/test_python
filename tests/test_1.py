class Test1:

    def test_click_login_button(self, setup_login_page):
        setup_login_page.click_login_btn()
        assert setup_login_page.is_url_login(), 'Página não encontrada!'
        assert setup_login_page.has_login_error_message(), 'Mensagem de erro não encontrada!'


