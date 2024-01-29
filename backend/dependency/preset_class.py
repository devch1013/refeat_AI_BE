from ai_module.src.models.llm.chain.summary_chain import SummaryChain
from ai_module.src.database.elastic_search.custom_elastic_search import CustomElasticSearch
from ai_module.src.database.knowledge_graph.graph_construct import KnowledgeGraphDataBase
from ai_module.src.modules.file_to_db.file_processor import FileProcessor
from ai_module.src.modules.chat.custom_chat_agent_module import ChatAgentModule
from ai_module.src.modules.add_column.data_extract_module import AddColumnModule

        
required_classes = {
    "SummaryChain": SummaryChain(),
    "CustomElasticSearch": CustomElasticSearch(index_name='refeat_ai', host="http://10.10.10.27:9200"),
    "KnowledgeGraphDatabase": KnowledgeGraphDataBase()
}


class AiModules:
    def __init__(self):
        print("init ai module!!!")
        summary_chain = SummaryChain()
        es = CustomElasticSearch(index_name='refeat_ai', host="http://10.10.10.27:9200")
        graph = KnowledgeGraphDataBase()
        self.file_processor: FileProcessor = FileProcessor(
        es=es,
        summary_chain=summary_chain,
        knowledge_graph_db=graph,
        json_save_dir="s3_mount/json/",
        screenshot_dir="s3_mount/screenshot/",
        html_save_dir="s3_mount/html/",
    )
        self.chat_agent: ChatAgentModule = ChatAgentModule(
        verbose=True, es=es, knowledge_graph_db=graph
    )
        self.column_module: AddColumnModule = AddColumnModule(es=es)
        
        