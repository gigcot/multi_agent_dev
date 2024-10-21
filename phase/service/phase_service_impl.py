from engine import ModelConfig
from phase.entity.phase_chat_turn_limit import PhaseChatTurnLimit
from phase.entity.phase_prompts import PhasePrompt
from phase.repository.code_complete.code_complete_phase_repository_impl import (
    CodeCompletePhaseRepositoryImpl,
)
from phase.repository.code_review_comment.code_review_comment_phase_repository_impl import (
    CodeReviewCommentPhaseRepositoryImpl,
)
from phase.repository.code_review_modification.code_review_modification_phase_repository_impl import (
    CodeReviewModificationPhaseRepositoryImpl,
)
from phase.repository.coding.code_phase_repository_impl import CodingPhaseRepositoryImpl
from phase.repository.demand_analysis.demand_analysis_phase_repository_impl import (
    DemandAnalysisPhaseResitoryImpl,
)
from phase.repository.language_choose.language_choose_phase_repository_impl import (
    LanguageChoosePhaseRepositoryImpl,
)
from phase.repository.manual.manual_phase_repository_impl import (
    ManualPhaseRepositoryImpl,
)
from phase.repository.test_error_summary.test_error_summary_phase_repository_impl import (
    TestErrorSummaryPhaseRepositoryImpl,
)
from phase.repository.test_modification.test_modification_phase_repository_impl import (
    TestModificationPhaseRepositoryImpl,
)
from phase.service.phase_service import PhaseService
from role_playing.entity.role_prompts import RolePrompt
from role_playing.entity.role_type import RoleType


class PhaseServiceImpl(PhaseService):
    def __init__(
        self,
        model_config: ModelConfig,
        phase_prompts: PhasePrompt = PhasePrompt(),
        role_types: RoleType = RoleType(),
        role_prompts: RolePrompt = RolePrompt(),
        phase_chat_turn_limit: PhaseChatTurnLimit = PhaseChatTurnLimit(),
    ):
        self.model_config = model_config
        self.phase_prompts = phase_prompts
        self.role_types = role_types
        self.role_prompts = role_prompts
        self.phase_chat_turn_limit = phase_chat_turn_limit

    def get_demand_analysis_phase(self):
        return DemandAnalysisPhaseResitoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.demand_analysis,
            assistant_role_name=self.role_types.CPO,
            assistant_role_prompt=self.role_prompts.CPO,
            user_role_name=self.role_types.CEO,
            user_role_prompt=self.role_prompts.CEO,
            chat_turn_limit=self.phase_chat_turn_limit.demand_analysis,
        )

    def get_language_choose_phase(self):
        return LanguageChoosePhaseRepositoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.language_choose,
            assistant_role_name=self.role_types.CTO,
            assistant_role_prompt=self.role_prompts.CTO,
            user_role_name=self.role_types.CEO,
            user_role_prompt=self.role_prompts.CEO,
            chat_turn_limit=self.phase_chat_turn_limit.language_choose,
        )

    def get_coding_phase(self):
        return CodingPhaseRepositoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.coding,
            assistant_role_name=self.role_types.PROGRAMMER,
            assistant_role_prompt=self.role_prompts.PROGRAMMER,
            user_role_name=self.role_types.CTO,
            user_role_prompt=self.role_prompts.CTO,
            chat_turn_limit=self.phase_chat_turn_limit.coding,
        )

    def get_code_complete_phase(self):
        return CodeCompletePhaseRepositoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.code_complete,
            assistant_role_name=self.role_types.PROGRAMMER,
            assistant_role_prompt=self.role_prompts.PROGRAMMER,
            user_role_name=self.role_types.CTO,
            user_role_prompt=self.role_prompts.CTO,
            chat_turn_limit=self.phase_chat_turn_limit.code_complete,
        )

    def get_code_review_comment_phase(self):
        return CodeReviewCommentPhaseRepositoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.code_review_comment,
            assistant_role_name=self.role_types.REVIEWER,
            assistant_role_prompt=self.role_prompts.REVIEWER,
            user_role_name=self.role_types.PROGRAMMER,
            user_role_prompt=self.role_prompts.PROGRAMMER,
            chat_turn_limit=self.phase_chat_turn_limit.code_review_comment,
        )

    def get_code_review_modification_phase(self):
        return CodeReviewModificationPhaseRepositoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.code_review_modification,
            assistant_role_name=self.role_types.REVIEWER,
            assistant_role_prompt=self.role_prompts.REVIEWER,
            user_role_name=self.role_types.PROGRAMMER,
            user_role_prompt=self.role_prompts.PROGRAMMER,
            chat_turn_limit=self.phase_chat_turn_limit.code_review_modification,
        )

    def get_test_error_summary_phase(self):
        return TestErrorSummaryPhaseRepositoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.test_error_summary,
            assistant_role_name=self.role_types.PROGRAMMER,
            assistant_role_prompt=self.role_prompts.PROGRAMMER,
            user_role_name=self.role_types.TESTER,
            user_role_prompt=self.role_prompts.TESTER,
            chat_turn_limit=self.phase_chat_turn_limit.test_error_summary,
        )

    def get_test_modification_phase(self):
        return TestModificationPhaseRepositoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.test_modification,
            assistant_role_name=self.role_types.PROGRAMMER,
            assistant_role_prompt=self.role_prompts.PROGRAMMER,
            user_role_name=self.role_types.TESTER,
            user_role_prompt=self.role_prompts.TESTER,
            chat_turn_limit=self.phase_chat_turn_limit.test_modification,
        )

    def get_manual_phase(self):
        return ManualPhaseRepositoryImpl(
            model_config=self.model_config,
            phase_prompt=self.phase_prompts.manual,
            assistant_role_name=self.role_types.CPO,
            assistant_role_prompt=self.role_prompts.CPO,
            user_role_name=self.role_types.CEO,
            user_role_prompt=self.role_prompts.CEO,
            chat_turn_limit=self.phase_chat_turn_limit.manual,
        )
