import unittest
import requests


class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5003/bookings"

    def test_booking_records(self):
        """ Test /bookings/<username> for all known bookings"""
        for date, expected in GOOD_RESPONSES.iteritems():
            reply = requests.get("{}/{}".format(self.url, date))
            actual_reply = reply.json()

            self.assertEqual(len(actual_reply), len(expected),
                             "Got {} booking but expected {}".format(
                                 len(actual_reply), len(expected)
                             ))

            self.assertEqual(set(actual_reply), set(expected),
                             "Got {} but expected {}".format(
                                 actual_reply, expected))

    def test_not_found(self):
        """ Test /showtimes/<date> for non-existent users"""
        invalid_user = "a"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_user))
        self.assertEqual(actual_reply.status_code, 404,
                         "Got {} but expected 404".format(
                             actual_reply.status_code))

GOOD_RESPONSES = {
  "egor_schukin": {
    "09022017": [
      "id4"
    ]
  },
  "yury_osipov": {
    "09022017": [
      "id4"
    ],
    "10022017": [
      "id6"
    ]
  },
  "larisa_burova": {
    "09022017": [
      "id5",
      "id4"
    ],
    "13022017": [
      "id2",
      "id6"
    ]
  }
}