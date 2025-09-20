benchmark_settings = {
   'activemq': {
        'log_file': 'activemq/activemq_full.log',
        'log_format': '<Content>',
        'regex': [
            r'0x[0-9a-fA-F]+',                # Hex transaction/session IDs
            r'\d+',                           # General numbers (counters, IDs, sizes)
            r'\[[^\]]+\]',                    # Square bracketed values (users, files, objects)
            r'(?:[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+)', # Email addresses
            r'(?:\d{1,3}\.){3}\d{1,3}',       # IPv4 addresses
            r'(?:https?|ftp|jdbc|ssh|ws|telnet|mailto|file|rtmp|smb|ldap|irc|git|tcp|amqp|mqtt|stomp|rmi|odbc|bluetooth|rdp)://[^\s]+', # URLs and connection strings
            r'queue://[^\s]+',                # Queue destinations
            r'topic://[^\s]+',                # Topic destinations
            r'temp-queue://[^\s]+',           # Temporary queue destinations
            r'temp-topic://[^\s]+',           # Temporary topic destinations
            r'(?<=Received: ).*',             # Received message content
            r'(?<=Creating message: ).*',     # Created message content
            r'(?<=Creating topic: ).*',       # Created topic names
            r'(?<=Creating queue: ).*',       # Created queue names
            r'(?<=Failed to ).*',             # Failure messages
            r'(?<=Error ).*',                 # Error messages
            r'(?<=Exception ).*',             # Exception messages
        ],
        'st': 0.4,
        'depth': 4
    },
    'cas': {
        'log_file': 'cas/cas_full.log',
        'log_format': '<Content>',
        'regex': [
            r'(?:https?|ftp|ldap|sftp|jdbc|ssh|ws|wss|telnet|mailto|file|rtmp|smb|irc|git|tcp|amqp|mqtt|stomp|rmi|odbc|bluetooth|rdp)://[^\s\]]+', # URLs and connection strings
            r'urn:[a-zA-Z0-9:.\-]+',                  # URNs (SAML, OASIS, etc.)
            r'\[[^\]]+\]',                            # Square bracketed values (attributes, codes, ids)
            r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', # Email addresses
            r'(?:\d{1,3}\.){3}\d{1,3}',               # IPv4 addresses
            r'[a-fA-F0-9:]{2,}',                      # IPv6 addresses and hex tokens
            r'\d+',                                   # General numbers (ids, counters, codes)
            r'[A-Z0-9\-]{2,}',                        # Ticket IDs, codes, etc.
            r'(?<=for \[)[^\]]+(?=\])',               # Values inside 'for [...]'
            r'(?<=service \[)[^\]]+(?=\])',           # Service names inside 'service [...]'
            r'(?<=principal \[)[^\]]+(?=\])',         # Principal names inside 'principal [...]'
            r'(?<=attribute \[)[^\]]+(?=\])',         # Attribute names inside 'attribute [...]'
            r'(?<=id \[)[^\]]+(?=\])',                # IDs inside 'id [...]'
            r'(?<=token \[)[^\]]+(?=\])',             # Tokens inside 'token [...]'
            r'(?<=password \[)[^\]]+(?=\])',          # Passwords inside 'password [...]'
            r'(?<=username \[)[^\]]+(?=\])',          # Usernames inside 'username [...]'
            r'(?<=client \[)[^\]]+(?=\])',            # Client names inside 'client [...]'
            r'(?<=provider \[)[^\]]+(?=\])',          # Provider names inside 'provider [...]'
            r'(?<=event \[)[^\]]+(?=\])',             # Event names inside 'event [...]'
            r'(?<=status \[)[^\]]+(?=\])',            # Status inside 'status [...]'
            r'(?<=role \[)[^\]]+(?=\])',              # Role inside 'role [...]'
        ],
        'st': 0.4,
        'depth': 4
    },
        'CoreNLP': {
        'log_file': 'CoreNLP/CoreNLP_full.log',
        'log_format': '<Content>',
        'regex': [
            r'\d{4}-\d{2}-\d{2}', # Date
            r'(?:\d+\.)+\d+',    # Version numbers or dotted numerics
            r'\d+',              # Integers
            r'/[^ ]+',           # File paths
            r'\[[^\]]+\]',       # Bracketed content
            r'"[^"]+"',          # Quoted content
            r'[a-zA-Z0-9\._-]+\.[a-zA-Z0-9\._-]+', # Class names or file names
        ],
        'st': 0.4,
        'depth': 4
    },
    'hive': {
        'log_file': 'hive/hive_full.log',
        'log_format': '<Content>',
        'regex': [
            r'/[^ ]+',
            r'[a-zA-Z0-9\._-]+\.[a-zA-Z0-9\._-]+',
            r'\[[^\]]+\]',
            r"'[^']+'",
            r'\d+',
        ],
        'st': 0.4,
        'depth': 4
    },
    'OpenSearch': {
        'log_file': 'OpenSearch/OpenSearch_full.log',
        'log_format': '<Content>',
        'regex': [
            r'(\d+\.){3}\d+',
            r'\d+',
            r'/[^ ]+',
            r'\[[^\]]+\]',
            r'[a-zA-Z0-9\._-]+\.[a-zA-Z0-9\._-]+',
        ],
        'st': 0.4,
        'depth': 4
    },
    'camel': {
        'log_file': 'camel/camel_full.log',
        'log_format': '<Content>',
        'regex': [
            r'(\d+\.){3}\d+', 
            r'\d+',
            r'0x[0-9a-fA-F]+',
            r'[a-zA-Z0-9\._-]+\.[a-zA-Z0-9\._-]+',
            r'\[[^\]]+\]',
            r'[a-zA-Z]+:\/\/[^\s]+'
        ],
        'st': 0.4,
        'depth': 4
    },
    'cassandra': {
        'log_file': 'cassandra/cassandra_full.log',
        'log_format': '<Content>',
        'regex': [
            r'(\d+\.){3}\d+',
            r'\d+',
            r'/[^ ]+',
            r'0x[0-9a-fA-F]+',
            r'\[[^\]]+\]',
            r'[a-zA-Z]+:\/\/[^\s]+',
            r'[a-zA-Z0-9\._-]+\.[a-zA-Z0-9\._-]+',
        ],
        'st': 0.4,
        'depth': 4
    },
    'hbase': {
        'log_file': 'hbase/hbase_full.log',
        'log_format': '<Content>',
        'regex': [
            r'(\d+\.){3}\d+',
            r'\d+',
            r'/[^ ]+',
            r'\[[^\]]+\]',
            r'0x[0-9a-fA-F]+',
            r'[a-zA-Z0-9\._-]+\.[a-zA-Z0-9\._-]+',
        ],
        'st': 0.4,
        'depth': 4
    },
    'jenkins': {
        'log_file': 'jenkins/jenkins_full.log',
        'log_format': '<Content>',
        'regex': [
            r'(\d+\.){3}\d+',
            r'\d+',
            r'/[^ ]+',
            r'\[[^\]]+\]',
            r'0x[0-9a-fA-F]+',
            r'[a-zA-Z0-9\._-]+\.[a-zA-Z0-9\._-]+',
        ],
        'st': 0.4,
        'depth': 4
    },
    'pytorch': {
        'log_file': 'pytorch/pytorch_full.log',
        'log_format': '<Content>',
        'regex': [r'(\d+\.){3}\d+', r'\d+'],
        'st': 0.4,
        'depth': 4
    },
}



























# benchmark_settings.update({
#     'activemq': {
#         'log_file': 'activemq/activemq_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#     },
#     'cas': {

#     'Hadoop': {
#         'log_file': 'Hadoop/Hadoop_2k.log',
#         'log_format': '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>',
#         'regex': [r'(\d+\.){3}\d+'],
#         'st': 0.5,
#         'depth': 4        
#         },

#     'Spark': {
#         'log_file': 'Spark/Spark_2k.log',
#         'log_format': '<Date> <Time> <Level> <Component>: <Content>', 
#         # 'regex': [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+'],
#         'regex': [],
#         'st': 0.5,
#         'depth': 4
#         },

#     'Zookeeper': {
#         'log_file': 'Zookeeper/Zookeeper_2k.log',
#         'log_format': '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>',
#         'regex': [r'(/|)(\d+\.){3}\d+(:\d+)?'],
#         'st': 0.5,
#         'depth': 4        
#         },

#     'BGL': {
#         'log_file': 'BGL/BGL_2k.log',
#         'log_format': '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>',
#         'regex': [r'core\.\d+'],
#         'st': 0.5,
#         'depth': 4        
#         },

#     'HPC': {
#         'log_file': 'HPC/HPC_2k.log',
#         'log_format': '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>',
#         'regex': [r'=\d+'],
#         'st': 0.5,
#         'depth': 4
#         },

#     'Thunderbird': {
#         'log_file': 'Thunderbird/Thunderbird_2k.log',
#         'log_format': '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>',
#         # 'regex': [r'(\d+\.){3}\d+'],
#         'regex': [],
#         'st': 0.5,
#         'depth': 4        
#         },

#     'Windows': {
#         'log_file': 'Windows/Windows_2k.log',
#         'log_format': '<Date> <Time>, <Level>                  <Component>    <Content>',
#         'regex': [r'0x.*?\s'],
#         'st': 0.7,
#         'depth': 5      
#         },

#     'Linux': {
#         'log_file': 'Linux/Linux_2k.log',
#         'log_format': '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}'],
#         'st': 0.39,
#         'depth': 6        
#         },

#     'Android': {
#         'log_file': 'Android/Android_2k.log',
#         'log_format': '<Date> <Time>  <Pid>  <Tid> <Level> <Component>: <Content>',
#         'regex': [r'(/[\w-]+)+', r'([\w-]+\.){2,}[\w-]+', r'\b(\-?\+?\d+)\b|\b0[Xx][a-fA-F\d]+\b|\b[a-fA-F\d]{4,}\b'],
#         'st': 0.2,
#         'depth': 6   
#         },

#     'HealthApp': {
#         'log_file': 'HealthApp/HealthApp_2k.log',
#         'log_format': '<Time>\|<Component>\|<Pid>\|<Content>',
#         'regex': [],
#         'st': 0.2,
#         'depth': 4
#         },

#     'Apache': {
#         'log_file': 'Apache/Apache_2k.log',
#         'log_format': '\[<Time>\] \[<Level>\] <Content>',
#         'regex': [r'(\d+\.){3}\d+'],
#         'st': 0.5,
#         'depth': 4        
#         },

#     'Proxifier': {
#         'log_file': 'Proxifier/Proxifier_2k.log',
#         'log_format': '\[<Time>\] <Program> - <Content>',
#         'regex': [r'<\d+\ssec', r'([\w-]+\.)+[\w-]+(:\d+)?', r'\d{2}:\d{2}(:\d{2})*', r'[KGTM]B'],
#         'st': 0.6,
#         'depth': 3
#         },

#     'OpenSSH': {
#         'log_file': 'OpenSSH/OpenSSH_2k.log',
#         'log_format': '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>',
#         'regex': [r'(\d+\.){3}\d+', r'([\w-]+\.){2,}[\w-]+'],
#         'st': 0.6,
#         'depth': 5   
#         },

#     'OpenStack': {
#         'log_file': 'OpenStack/OpenStack_2k.log',
#         'log_format': '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>',
#         'regex': [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+'],
#         'st': 0.5,
#         'depth': 5
#         },

#     'Mac': {
#         'log_file': 'Mac/Mac_2k.log',
#         'log_format': '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>',
#         'regex': [r'([\w-]+\.){2,}[\w-]+'],
#         'st': 0.7,
#         'depth': 6   
#         },

#     #    Added LogBase datasets below

#     'brave': {
#         'log_file': 'brave/brave_full.log',
#         'log_format': '<Content>',
#         'regex': [r'\d+', r'\[[a-z]+\]'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'airflow': {
#         'log_file': 'airflow/airflow_full.log',
#         'log_format': '<Content>',
#         'regex': [r'\[[a-z/]+\]', r'\d+', r'[\w-]+\.(json|pdf|csv|sql|xml|conf|zip|html|sh|mp4)'],
#         'st': 0.3,
#         'depth': 5
#         },
#     'dbeaver': {
#         'log_file': 'dbeaver/dbeaver_full.log',
#         'log_format': '<Content>',
#         'regex': [r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'pytorch': {
#         'log_file': 'pytorch/pytorch_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'transformers': {
#         'log_file': 'transformers/transformers_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'flink': {
#         'log_file': 'flink/flink_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'presto': {
#         'log_file': 'presto/presto_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'cassandra': {
#         'log_file': 'cassandra/cassandra_full.log',
#         'log_format': '<Content>',
#         'regex': [],
#         'st': 0.4,
#         'depth': 4
#         },
#     'liquibase': {
#         'log_file': 'liquibase/liquibase_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'jenkins': {
#         'log_file': 'jenkins/jenkins_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'maven': {
#         'log_file': 'maven/maven_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'spring-boot': {
#         'log_file': 'spring-boot/spring-boot_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'netty': {
#         'log_file': 'netty/netty_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'activemq': {
#         'log_file': 'activemq/activemq_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'rocketmq': {
#         'log_file': 'rocketmq/rocketmq_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'elasticsearch': {
#         'log_file': 'elasticsearch/elasticsearch_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'logstash': {
#         'log_file': 'logstash/logstash_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'cas': {
#         'log_file': 'cas/cas_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'shenyu': {
#         'log_file': 'shenyu/shenyu_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'cpython': {
#         'log_file': 'cpython/cpython_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'Python': {
#         'log_file': 'Python/Python_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'jitsi': {
#         'log_file': 'jitsi/jitsi_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'openpilot': {
#         'log_file': 'openpilot/openpilot_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },
#     'javacv': {
#         'log_file': 'javacv/javacv_full.log',
#         'log_format': '<Content>',
#         'regex': [r'(\d+\.){3}\d+', r'\d+'],
#         'st': 0.4,
#         'depth': 4
#         },

#     }