from django.test import TestCase, Client
# from django.urls import reverse, resolve, Resolver404

"""
Django Unit Tests for Yearbook Month URLs

This test suite validates:
1. The yearbook month URL resolves and returns 200 for valid year/month.
2. Edge cases: empty, invalid, or out-of-range year/month return 404.
"""
class YearbookMonthURLTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # If you have a named URL pattern, use reverse('yearbook-month', args=[year, month])
        # Otherwise, use the hardcoded path as below:
        self.url_template = '/yearbook/{year}/{month}/'

    def test_valid_year_and_month(self):
        # Test lower and upper bounds
        for year in [2000, 2024, 2100]:
            for month in [1, 6, 12]:
                url = self.url_template.format(year=year, month=month)
                response = self.client.get(url)
                # If you have a view, you may want to check for 200, otherwise 404 if not implemented
                self.assertEqual(response.status_code, 200)

    def test_valid_year_and_month_in_HTML(self):
        # Test a specific valid year/month and check content
        for year in [2000, 2024, 2100]:
            month_index = 0
            for month in [1, 6, 12]:
                url = self.url_template.format(year=year, month=month)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, str(year))
                self.assertContains(response, ["January", "June", "December"][month_index])
                month_index += 1
                
    def test_year_below_range(self):
        url = self.url_template.format(year=1999, month=5)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_year_above_range(self):
        url = self.url_template.format(year=2101, month=5)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_month_below_range(self):
        url = self.url_template.format(year=2024, month=0)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_month_above_range(self):
        url = self.url_template.format(year=2024, month=13)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_empty_year(self):
        url = '/yearbook//5/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_empty_month(self):
        url = '/yearbook/2024//'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_non_integer_year(self):
        url = self.url_template.format(year='abcd', month=5)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_non_integer_month(self):
        url = self.url_template.format(year=2024, month='xyz')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_missing_both_fields(self):
        url = '/yearbook//'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
