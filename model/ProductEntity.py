from core.BaseEntity import BaseEntity


class ProductEntity(BaseEntity):
    def __init__(self):
        super(ProductEntity, self).__init__()
        self.table = "product"  # 序号
        self.productId = None  # 商品ID
        self.productName = None  # 商品名称
        self.attrId = None  # 规格ID
        self.unitId = None  # 单位ID
        self.canKapPrice = None  # 参考价
        self.lingShouPrice = None  # 零售价
        self.vipPrice = None  # 会员价
        self.piFaPrice = None  # 批发价
        self.defaultSupplier = None  # 默认供应商
        self.categoryId = None  # 所属类别
        self.initStock = None  # 初始库存
        self.minLimit = None  # 缺货下限
        self.maxLimit = None  # 积压上限
        self.desc = None  # 商品说明
