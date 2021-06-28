import re

FIRST_INPUT_GREETING = "Hello! Please write down an e-mail box name to find wether it is valid...:"
EVERY_NEXT_INPUT_GREETING = "Hello again! Please write down an e-mail box name to find wether it is valid...:"


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass


def read_input_line(*args):
    input_line = input(f"{''.join(args)}")
    return input_line


def check_mailbox_for__at__container(mailbox):
    """check for at='@' symbol"""
    return mailbox.count("@") == 1


def check_mailbox_domain(mailbox):
    """using working regex for email validator, not the best one, but works just fine"""
    regex = r"@[a-z]+(\.[com|bg|org|net]+$)"
    is_mailbox = "".join([obj.group() for obj in re.finditer(regex, mailbox)])
    return is_mailbox


def check_mailbox_length(mailbox):
    """checking for length of symbols bfore @ symbol"""
    at_sign_index = mailbox.index("@")
    return len(mailbox[:at_sign_index]) >= 4


def main(_input_):
    while not _input_ == "End":
        if not check_mailbox_for__at__container(_input_):
            raise MustContainAtSymbolError("Email must contain @")
        elif not check_mailbox_domain(_input_):
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        elif not check_mailbox_length(_input_):
            raise NameTooShortError("Name must be more than 4 characters")
        print(_input_)
        _input_ = read_input_line(EVERY_NEXT_INPUT_GREETING)


read_line = read_input_line(FIRST_INPUT_GREETING)
solution_result = main(read_line)
