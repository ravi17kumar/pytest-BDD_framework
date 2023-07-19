Feature: for_task

  Scenario: verify user is not able to login with wrong email
        Given launching URL in chrome browser
        Then verify that user will redirected to hubspot
        When user will able to enter username and pwd so that they will click on login button
        Then verify user is not able to login

    