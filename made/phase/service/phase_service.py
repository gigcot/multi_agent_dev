from abc import ABC, abstractmethod


class PhaseService(ABC):
    @abstractmethod
    def get_demand_analysis_phase(self, chat_turn_limit):
        pass

    @abstractmethod
    def get_language_choose_phase(self, chat_turn_limit):
        pass

    @abstractmethod
    def get_coding_phase(self, chat_turn_limit):
        pass

    @abstractmethod
    def get_code_complete_phase(self, chat_turn_limit):
        pass

    @abstractmethod
    def get_code_review_comment_phase(self, chat_turn_limit):
        pass

    @abstractmethod
    def get_code_review_modification_phase(self, chat_turn_limit):
        pass

    @abstractmethod
    def get_test_error_summary_phase(self, chat_turn_limit):
        pass

    @abstractmethod
    def get_test_modification_phase(self, chat_turn_limit):
        pass

    @abstractmethod
    def get_manual_phase(self, chat_turn_limit):
        pass
