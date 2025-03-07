class CommonObject:
    def get(self, property_name):
        """
        プロパティの値を取得するメソッド

        Args:
            property_name (str): プロパティ名
        Returns:
            プロパティの値
        Raises:
            AttributeError: 指定されたプロパティが存在しない場合

        """
        try:
            return getattr(self, property_name)
        except AttributeError:
            print('指定されたプロパティは存在しません')
            return None
    
    def set(self, property_name, value):
        """
        プロパティの値を設定するメソッド

        Args:
            property_name (str): プロパティ名
            value: プロパティの値
        Returns:
            None
        Raises:
            AttributeError: 指定されたプロパティが存在しない場合
            
        """
        try: 
            setattr(self, property_name, value)
        except AttributeError:
            print('指定されたプロパティは存在しません')
            return None