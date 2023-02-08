class ReadReplicaRouter:
    """
    AWS readReplica RDS 에서 데이터 읽도록 변경 라우터
    """

    def db_for_read(self, model, **hints):
        return 'replica'

    def db_for_write(self, model, **hints):
        return 'default'
