# -*- coding: utf-8 -*-
"""Mahak AI-PoweredChatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jd3l2Mp9fHddTqY-Tp3Epl4wD2JA3AQG
"""

import re
import random

import random
import re

class RuleBot:
    # Potential Negative Responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # Exit Conversation Keywords
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # Random Starter Questions
    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does earth have a leader?",
        "What planets have you visited?",
        "What technology do you have on this planet?"
    )

    def __init__(self):
        self.alienbabble = {
            "describe_planet_intent": r".*\byour planet\b.*",
            "answer_why_intent": r"why\sare.*",
            "about_MahakChatbot": r".*\bMahakChatbot\b.*"
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am MahakChatbot. Will you help me learn about your planet?\n"
        ).lower()
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
        else:
            self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Ok, have a nice Earth day!")
                return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_questions) + "\n").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.search(regex_pattern, reply)
            if found_match:
                if intent == "describe_planet_intent":
                    return self.describe_planet_intent()
                elif intent == "answer_why_intent":
                    return self.answer_why_intent()
                elif intent == "about_MahakChatbot":
                    return self.about_MahakChatbot()
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = [
            "My planet is a utopia of diverse organisms and species.\n",
            "I am from Opidipus, the capital of the Wayward Galaxies.\n"
        ]
        return random.choice(responses)

    def answer_why_intent(self):
        responses = [
            "I come in peace.\n",
            "I am here to collect data on your planet and its inhabitants.\n",
            "I heard the coffee is good.\n"
        ]
        return random.choice(responses)

    def about_MahakChatbot(self):
        responses = [
            "MahakChatbot is here to collect data on your planet and its inhabitants.\n",
            "MahakChatbot is here to help you.\n"
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responses = [
            "Please tell me more.\n",
            "Tell me more!\n",
            "Why do you say that?\n",
            "I see. Can you elaborate?\n",
            "Interesting. Can you tell me more?\n",
            "I see. How do you think?\n",
            "Why?\n",
            "How do you think I feel when you say that?\n"
        ]
        return random.choice(responses)

# Instantiate and run the chatbot
AlienBot = RuleBot()
AlienBot.greet()