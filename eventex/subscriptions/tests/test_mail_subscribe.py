from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Túlio César Gaio", cpf="07101281699", email="tuliogaio@gmail.com", phone="94992415990")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'gmvhorasextras@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['gmvhorasextras@gmail.com', 'tuliogaio@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscrition_email_body(self):
        contents = ['Túlio César Gaio', '07101281699', 'tuliogaio@gmail.com', '94992415990']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
