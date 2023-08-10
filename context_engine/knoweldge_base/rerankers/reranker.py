from abc import ABC, abstractmethod
from typing import List

from context_engine.knoweldge_base.models import KBQueryResult


class Reranker(ABC):

    @abstractmethod
    def rerank_results(self,
                       results: List[KBQueryResult]
                       ) -> List[KBQueryResult]:
        pass

    @abstractmethod
    async def arerank_results(self,
                              results: List[KBQueryResult]
                              ) -> List[KBQueryResult]:
        pass


class TransparentReranker(Reranker):
    def rerank_results(self,
                       results: List[KBQueryResult]
                       ) -> List[KBQueryResult]:
        return results

    async def arerank_results(self,
                              results: List[KBQueryResult]
                              ) -> List[KBQueryResult]:
        return results
