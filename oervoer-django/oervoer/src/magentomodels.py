# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AdminAssert(models.Model):
    assert_id = models.AutoField(primary_key=True)
    assert_type = models.CharField(max_length=20, blank=True, null=True)
    assert_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_assert'


class AdminRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    tree_level = models.SmallIntegerField()
    sort_order = models.SmallIntegerField()
    role_type = models.CharField(max_length=1)
    user_id = models.IntegerField()
    role_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_role'


class AdminRule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(AdminRole)
    resource_id = models.CharField(max_length=255, blank=True, null=True)
    privileges = models.CharField(max_length=20, blank=True, null=True)
    assert_id = models.IntegerField()
    role_type = models.CharField(max_length=1, blank=True, null=True)
    permission = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_rule'


class AdminUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(unique=True, max_length=40, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    logdate = models.DateTimeField(blank=True, null=True)
    lognum = models.SmallIntegerField()
    reload_acl_flag = models.SmallIntegerField()
    is_active = models.SmallIntegerField()
    extra = models.TextField(blank=True, null=True)
    rp_token = models.TextField(blank=True, null=True)
    rp_token_created_at = models.DateTimeField(blank=True, null=True)
    jirafe_send_email_for_store = models.CharField(max_length=255, blank=True, null=True)
    jirafe_send_email = models.IntegerField(blank=True, null=True)
    jirafe_email_report_type = models.CharField(max_length=255, blank=True, null=True)
    jirafe_user_id = models.CharField(max_length=255, blank=True, null=True)
    jirafe_user_token = models.CharField(max_length=255, blank=True, null=True)
    jirafe_email_suppress = models.IntegerField(blank=True, null=True)
    jirafe_dashboard_active = models.IntegerField(blank=True, null=True)
    jirafe_optin_answered = models.IntegerField(blank=True, null=True)
    jirafe_enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user'


class AdminnotificationInbox(models.Model):
    notification_id = models.AutoField(primary_key=True)
    severity = models.SmallIntegerField()
    date_added = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.SmallIntegerField()
    is_remove = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'adminnotification_inbox'


class AmNotfoundAttempt(models.Model):
    attempt_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    user = models.CharField(max_length=255)
    client_ip = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'am_notfound_attempt'


class AmNotfoundError(models.Model):
    error_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    type = models.IntegerField()
    error = models.TextField()

    class Meta:
        managed = False
        db_table = 'am_notfound_error'


class AmNotfoundLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    store_id = models.SmallIntegerField()
    date = models.DateTimeField()
    url = models.CharField(max_length=255)
    referer = models.TextField()
    client_ip = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'am_notfound_log'


class AmShiprulesAttribute(models.Model):
    attr_id = models.AutoField(primary_key=True)
    rule = models.ForeignKey('AmShiprulesRule')
    code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'am_shiprules_attribute'


class AmShiprulesRule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    is_active = models.IntegerField()
    calc = models.IntegerField()
    ignore_promo = models.IntegerField()
    pos = models.IntegerField()
    price_from = models.DecimalField(max_digits=12, decimal_places=2)
    price_to = models.DecimalField(max_digits=12, decimal_places=2)
    weight_from = models.DecimalField(max_digits=12, decimal_places=4)
    weight_to = models.DecimalField(max_digits=12, decimal_places=4)
    qty_from = models.IntegerField()
    qty_to = models.IntegerField()
    rate_base = models.DecimalField(max_digits=12, decimal_places=2)
    rate_fixed = models.DecimalField(max_digits=12, decimal_places=2)
    rate_percent = models.FloatField()
    rate_min = models.DecimalField(max_digits=12, decimal_places=2)
    rate_max = models.DecimalField(max_digits=12, decimal_places=2)
    handling = models.FloatField()
    name = models.CharField(max_length=255, blank=True, null=True)
    stores = models.CharField(max_length=255)
    cust_groups = models.CharField(max_length=255)
    carriers = models.TextField(blank=True, null=True)
    methods = models.TextField(blank=True, null=True)
    coupon = models.CharField(max_length=255, blank=True, null=True)
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_shiprules_rule'


class AmTableMethod(models.Model):
    method_id = models.AutoField(primary_key=True)
    is_active = models.IntegerField()
    pos = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    stores = models.CharField(max_length=255)
    cust_groups = models.CharField(max_length=255)
    select_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'am_table_method'


class AmTableRate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    method_id = models.IntegerField()
    country = models.CharField(max_length=4)
    state = models.IntegerField()
    city = models.CharField(max_length=100)
    zip_from = models.CharField(max_length=10)
    zip_to = models.CharField(max_length=10)
    price_from = models.DecimalField(max_digits=12, decimal_places=2)
    price_to = models.DecimalField(max_digits=12, decimal_places=2)
    weight_from = models.DecimalField(max_digits=12, decimal_places=4)
    weight_to = models.DecimalField(max_digits=12, decimal_places=4)
    qty_from = models.IntegerField()
    qty_to = models.IntegerField()
    shipping_type = models.IntegerField()
    cost_base = models.DecimalField(max_digits=12, decimal_places=2)
    cost_percent = models.DecimalField(max_digits=5, decimal_places=2)
    cost_product = models.DecimalField(max_digits=12, decimal_places=2)
    cost_weight = models.DecimalField(max_digits=12, decimal_places=2)
    time_delivery = models.CharField(max_length=255, blank=True, null=True)
    num_zip_from = models.IntegerField()
    num_zip_to = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'am_table_rate'
        unique_together = (('method_id', 'country', 'state', 'city', 'zip_from', 'zip_to', 'price_from', 'price_to', 'weight_from', 'weight_to', 'qty_from', 'qty_to', 'shipping_type'),)


class AmastyAmdeliverydateDeliverydate(models.Model):
    deliverydate_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('SalesFlatOrder')
    increment_id = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    reminder = models.IntegerField()
    tinterval_id = models.IntegerField(blank=True, null=True)
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'amasty_amdeliverydate_deliverydate'


class AmastyAmdeliverydateDinterval(models.Model):
    dinterval_id = models.AutoField(primary_key=True)
    store_ids = models.CharField(max_length=255)
    from_year = models.SmallIntegerField()
    from_month = models.SmallIntegerField()
    from_day = models.SmallIntegerField()
    to_year = models.SmallIntegerField()
    to_month = models.SmallIntegerField()
    to_day = models.SmallIntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'amasty_amdeliverydate_dinterval'


class AmastyAmdeliverydateHolidays(models.Model):
    holiday_id = models.AutoField(primary_key=True)
    store_ids = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    month = models.SmallIntegerField()
    day = models.SmallIntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'amasty_amdeliverydate_holidays'


class AmastyAmdeliverydateTinterval(models.Model):
    tinterval_id = models.AutoField(primary_key=True)
    store_ids = models.CharField(max_length=255)
    time_from = models.CharField(max_length=255)
    time_from_sql = models.CharField(max_length=255)
    time_to = models.CharField(max_length=255)
    time_to_sql = models.CharField(max_length=255)
    sorting_order = models.SmallIntegerField()
    quota = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amasty_amdeliverydate_tinterval'


class Api2AclAttribute(models.Model):
    entity_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=20)
    resource_id = models.CharField(max_length=255)
    operation = models.CharField(max_length=20)
    allowed_attributes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api2_acl_attribute'
        unique_together = (('user_type', 'resource_id', 'operation'),)


class Api2AclRole(models.Model):
    entity_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    role_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'api2_acl_role'


class Api2AclRule(models.Model):
    entity_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Api2AclRole)
    resource_id = models.CharField(max_length=255)
    privilege = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api2_acl_rule'
        unique_together = (('role_id', 'resource_id', 'privilege'),)


class Api2AclUser(models.Model):
    admin = models.ForeignKey(AdminUser, unique=True)
    role = models.ForeignKey(Api2AclRole)

    class Meta:
        managed = False
        db_table = 'api2_acl_user'


class ApiAssert(models.Model):
    assert_id = models.AutoField(primary_key=True)
    assert_type = models.CharField(max_length=20, blank=True, null=True)
    assert_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_assert'


class ApiRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    tree_level = models.SmallIntegerField()
    sort_order = models.SmallIntegerField()
    role_type = models.CharField(max_length=1)
    user_id = models.IntegerField()
    role_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_role'


class ApiRule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(ApiRole)
    resource_id = models.CharField(max_length=255, blank=True, null=True)
    api_privileges = models.CharField(max_length=20, blank=True, null=True)
    assert_id = models.IntegerField()
    role_type = models.CharField(max_length=1, blank=True, null=True)
    api_permission = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_rule'


class ApiSession(models.Model):
    user = models.ForeignKey('ApiUser')
    logdate = models.DateTimeField()
    sessid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_session'


class ApiUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    api_key = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    lognum = models.SmallIntegerField()
    reload_acl_flag = models.SmallIntegerField()
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_user'


class AwBlog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    post_content = models.TextField()
    status = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(unique=True, max_length=255)
    user = models.CharField(max_length=255)
    update_user = models.CharField(max_length=255)
    meta_keywords = models.TextField()
    meta_description = models.TextField()
    comments = models.IntegerField()
    tags = models.TextField()
    short_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'aw_blog'


class AwBlogCat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    meta_keywords = models.TextField()
    meta_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'aw_blog_cat'


class AwBlogCatStore(models.Model):
    cat_id = models.SmallIntegerField(blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aw_blog_cat_store'


class AwBlogComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.SmallIntegerField()
    comment = models.TextField()
    status = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'aw_blog_comment'


class AwBlogPostCat(models.Model):
    cat_id = models.SmallIntegerField(blank=True, null=True)
    post_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aw_blog_post_cat'


class AwBlogStore(models.Model):
    post_id = models.SmallIntegerField(blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aw_blog_store'


class AwBlogTags(models.Model):
    tag = models.CharField(max_length=255)
    tag_count = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aw_blog_tags'


class Bannerslider(models.Model):
    bannerslider_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    weblink = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    stores = models.TextField(blank=True, null=True)
    is_home = models.IntegerField()
    categories = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bannerslider'


class Bestseller(models.Model):
    bestseller_id = models.AutoField(primary_key=True)
    sku = models.ForeignKey('CatalogProductEntity', db_column='sku')
    product = models.ForeignKey('CatalogProductEntity')

    class Meta:
        managed = False
        db_table = 'bestseller'


class Bestsellerproducts(models.Model):
    bestsellerproducts_id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    products_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bestsellerproducts'


class BuckarooCertificates(models.Model):
    certificate_id = models.AutoField(primary_key=True)
    certificate = models.TextField()
    certificate_name = models.CharField(unique=True, max_length=255)
    upload_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'buckaroo_certificates'


class CaptchaLog(models.Model):
    type = models.CharField(max_length=32)
    value = models.CharField(max_length=32)
    count = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'captcha_log'
        unique_together = (('type', 'value'),)


class CatalogCategoryAncCategsIndexIdx(models.Model):
    category_id = models.IntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_anc_categs_index_idx'


class CatalogCategoryAncCategsIndexTmp(models.Model):
    category_id = models.IntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_anc_categs_index_tmp'


class CatalogCategoryAncProductsIndexIdx(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_anc_products_index_idx'


class CatalogCategoryAncProductsIndexTmp(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_anc_products_index_tmp'


class CatalogCategoryEntity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute_set_id = models.SmallIntegerField()
    parent_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=255)
    position = models.IntegerField()
    level = models.IntegerField()
    children_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_entity'


class CatalogCategoryEntityDatetime(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogCategoryEntity)
    value = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_datetime'
        unique_together = (('entity_type_id', 'entity_id', 'attribute_id', 'store_id'),)


class CatalogCategoryEntityDecimal(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogCategoryEntity)
    value = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_decimal'
        unique_together = (('entity_type_id', 'entity_id', 'attribute_id', 'store_id'),)


class CatalogCategoryEntityInt(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogCategoryEntity)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_int'
        unique_together = (('entity_type_id', 'entity_id', 'attribute_id', 'store_id'),)


class CatalogCategoryEntityText(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogCategoryEntity)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_text'
        unique_together = (('entity_type_id', 'entity_id', 'attribute_id', 'store_id'),)


class CatalogCategoryEntityVarchar(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogCategoryEntity)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_varchar'
        unique_together = (('entity_type_id', 'entity_id', 'attribute_id', 'store_id'),)


class CatalogCategoryFlatStore1(models.Model):
    entity = models.ForeignKey(CatalogCategoryEntity, primary_key=True)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=255)
    position = models.IntegerField()
    level = models.IntegerField()
    children_count = models.IntegerField()
    store = models.ForeignKey('CoreStore')
    all_children = models.TextField(blank=True, null=True)
    available_sort_by = models.TextField(blank=True, null=True)
    category_description_tpl = models.TextField(blank=True, null=True)
    category_meta_description_tpl = models.TextField(blank=True, null=True)
    category_meta_keywords_tpl = models.TextField(blank=True, null=True)
    category_meta_title_tpl = models.TextField(blank=True, null=True)
    category_title_tpl = models.TextField(blank=True, null=True)
    cdbp = models.TextField(blank=True, null=True)
    children = models.TextField(blank=True, null=True)
    custom_apply_to_products = models.IntegerField(blank=True, null=True)
    custom_design = models.CharField(max_length=255, blank=True, null=True)
    custom_design_from = models.DateTimeField(blank=True, null=True)
    custom_design_to = models.DateTimeField(blank=True, null=True)
    custom_layout_update = models.TextField(blank=True, null=True)
    custom_use_parent_settings = models.IntegerField(blank=True, null=True)
    default_sort_by = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    display_mode = models.CharField(max_length=255, blank=True, null=True)
    filter_description_tpl = models.TextField(blank=True, null=True)
    filter_meta_description_tpl = models.TextField(blank=True, null=True)
    filter_meta_keywords_tpl = models.TextField(blank=True, null=True)
    filter_meta_title_tpl = models.TextField(blank=True, null=True)
    filter_price_range = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    filter_title_tpl = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    include_in_menu = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_anchor = models.IntegerField(blank=True, null=True)
    landing_page = models.IntegerField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    page_layout = models.CharField(max_length=255, blank=True, null=True)
    path_in_store = models.TextField(blank=True, null=True)
    product_description_tpl = models.TextField(blank=True, null=True)
    product_full_description_tpl = models.TextField(blank=True, null=True)
    product_meta_description_tpl = models.TextField(blank=True, null=True)
    product_meta_keywords_tpl = models.TextField(blank=True, null=True)
    product_meta_title_tpl = models.TextField(blank=True, null=True)
    product_short_description_tpl = models.TextField(blank=True, null=True)
    product_title_tpl = models.TextField(blank=True, null=True)
    searchindex_weight = models.TextField(blank=True, null=True)
    seo_page_header = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    umm_cat_label = models.CharField(max_length=255, blank=True, null=True)
    umm_cat_target = models.CharField(max_length=255, blank=True, null=True)
    umm_dd_blocks = models.TextField(blank=True, null=True)
    umm_dd_columns = models.IntegerField(blank=True, null=True)
    umm_dd_proportions = models.CharField(max_length=255, blank=True, null=True)
    umm_dd_type = models.CharField(max_length=255, blank=True, null=True)
    umm_dd_width = models.CharField(max_length=255, blank=True, null=True)
    url_key = models.CharField(max_length=255, blank=True, null=True)
    url_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_flat_store_1'


class CatalogCategoryProduct(models.Model):
    category = models.ForeignKey(CatalogCategoryEntity)
    product = models.ForeignKey('CatalogProductEntity')
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product'
        unique_together = (('category_id', 'product_id'),)


class CatalogCategoryProductIndex(models.Model):
    category = models.ForeignKey(CatalogCategoryEntity)
    product = models.ForeignKey('CatalogProductEntity')
    position = models.IntegerField(blank=True, null=True)
    is_parent = models.SmallIntegerField()
    store = models.ForeignKey('CoreStore')
    visibility = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index'
        unique_together = (('category_id', 'product_id', 'store_id'),)


class CatalogCategoryProductIndexEnblIdx(models.Model):
    product_id = models.IntegerField()
    visibility = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index_enbl_idx'


class CatalogCategoryProductIndexEnblTmp(models.Model):
    product_id = models.IntegerField()
    visibility = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index_enbl_tmp'


class CatalogCategoryProductIndexIdx(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    position = models.IntegerField()
    is_parent = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    visibility = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index_idx'


class CatalogCategoryProductIndexTmp(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    position = models.IntegerField()
    is_parent = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    visibility = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index_tmp'


class CatalogCompareItem(models.Model):
    catalog_compare_item_id = models.AutoField(primary_key=True)
    visitor_id = models.IntegerField()
    customer = models.ForeignKey('CustomerEntity', blank=True, null=True)
    product = models.ForeignKey('CatalogProductEntity')
    store = models.ForeignKey('CoreStore', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_compare_item'


class CatalogEavAttribute(models.Model):
    attribute = models.ForeignKey('EavAttribute', primary_key=True)
    frontend_input_renderer = models.CharField(max_length=255, blank=True, null=True)
    is_global = models.SmallIntegerField()
    is_visible = models.SmallIntegerField()
    is_searchable = models.SmallIntegerField()
    is_filterable = models.SmallIntegerField()
    is_comparable = models.SmallIntegerField()
    is_visible_on_front = models.SmallIntegerField()
    is_html_allowed_on_front = models.SmallIntegerField()
    is_used_for_price_rules = models.SmallIntegerField()
    is_filterable_in_search = models.SmallIntegerField()
    used_in_product_listing = models.SmallIntegerField()
    used_for_sort_by = models.SmallIntegerField()
    is_configurable = models.SmallIntegerField()
    apply_to = models.CharField(max_length=255, blank=True, null=True)
    is_visible_in_advanced_search = models.SmallIntegerField()
    position = models.IntegerField()
    is_wysiwyg_enabled = models.SmallIntegerField()
    is_used_for_promo_rules = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_eav_attribute'


class CatalogProductBundleOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('CatalogProductEntity')
    required = models.SmallIntegerField()
    position = models.IntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_option'


class CatalogProductBundleOptionValue(models.Model):
    value_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(CatalogProductBundleOption)
    store_id = models.SmallIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_option_value'
        unique_together = (('option_id', 'store_id'),)


class CatalogProductBundlePriceIndex(models.Model):
    entity = models.ForeignKey('CatalogProductEntity')
    website = models.ForeignKey('CoreWebsite')
    customer_group = models.ForeignKey('CustomerGroup')
    min_price = models.DecimalField(max_digits=12, decimal_places=4)
    max_price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_price_index'
        unique_together = (('entity_id', 'website_id', 'customer_group_id'),)


class CatalogProductBundleSelection(models.Model):
    selection_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(CatalogProductBundleOption)
    parent_product_id = models.IntegerField()
    product = models.ForeignKey('CatalogProductEntity')
    position = models.IntegerField()
    is_default = models.SmallIntegerField()
    selection_price_type = models.SmallIntegerField()
    selection_price_value = models.DecimalField(max_digits=12, decimal_places=4)
    selection_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    selection_can_change_qty = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_selection'


class CatalogProductBundleSelectionPrice(models.Model):
    selection = models.ForeignKey(CatalogProductBundleSelection)
    website = models.ForeignKey('CoreWebsite')
    selection_price_type = models.SmallIntegerField()
    selection_price_value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_selection_price'
        unique_together = (('selection_id', 'website_id'),)


class CatalogProductBundleStockIndex(models.Model):
    entity_id = models.IntegerField()
    website_id = models.SmallIntegerField()
    stock_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    stock_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_stock_index'
        unique_together = (('entity_id', 'website_id', 'stock_id', 'option_id'),)


class CatalogProductEnabledIndex(models.Model):
    product = models.ForeignKey('CatalogProductEntity')
    store = models.ForeignKey('CoreStore')
    visibility = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_enabled_index'
        unique_together = (('product_id', 'store_id'),)


class CatalogProductEntity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute_set = models.ForeignKey('EavAttributeSet')
    type_id = models.CharField(max_length=32)
    sku = models.CharField(max_length=64, blank=True, null=True)
    has_options = models.SmallIntegerField()
    required_options = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    absolute_price = models.IntegerField()
    absolute_weight = models.IntegerField()
    sku_policy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_entity'


class CatalogProductEntityDatetime(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogProductEntity)
    value = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_datetime'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class CatalogProductEntityDecimal(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogProductEntity)
    value = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_decimal'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class CatalogProductEntityGallery(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogProductEntity)
    position = models.IntegerField()
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_gallery'
        unique_together = (('entity_type_id', 'entity_id', 'attribute_id', 'store_id'),)


class CatalogProductEntityGroupPrice(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(CatalogProductEntity)
    all_groups = models.SmallIntegerField()
    customer_group = models.ForeignKey('CustomerGroup')
    value = models.DecimalField(max_digits=12, decimal_places=4)
    website = models.ForeignKey('CoreWebsite')

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_group_price'
        unique_together = (('entity_id', 'all_groups', 'customer_group_id', 'website_id'),)


class CatalogProductEntityInt(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.IntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogProductEntity)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_int'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class CatalogProductEntityMediaGallery(models.Model):
    value_id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CatalogProductEntity)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_media_gallery'


class CatalogProductEntityMediaGalleryValue(models.Model):
    value = models.ForeignKey(CatalogProductEntityMediaGallery)
    store = models.ForeignKey('CoreStore')
    label = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    disabled = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_media_gallery_value'
        unique_together = (('value_id', 'store_id'),)


class CatalogProductEntityText(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.IntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogProductEntity)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_text'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class CatalogProductEntityTierPrice(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(CatalogProductEntity)
    all_groups = models.SmallIntegerField()
    customer_group = models.ForeignKey('CustomerGroup')
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    website = models.ForeignKey('CoreWebsite')

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_tier_price'
        unique_together = (('entity_id', 'all_groups', 'customer_group_id', 'qty', 'website_id'),)


class CatalogProductEntityVarchar(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type_id = models.IntegerField()
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    entity = models.ForeignKey(CatalogProductEntity)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_varchar'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class CatalogProductFlat1(models.Model):
    entity = models.ForeignKey(CatalogProductEntity, primary_key=True)
    attribute_set_id = models.SmallIntegerField()
    type_id = models.CharField(max_length=32)
    cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    gift_message_available = models.SmallIntegerField(blank=True, null=True)
    has_options = models.SmallIntegerField()
    image_label = models.CharField(max_length=255, blank=True, null=True)
    is_recurring = models.SmallIntegerField(blank=True, null=True)
    links_exist = models.IntegerField(blank=True, null=True)
    links_purchased_separately = models.IntegerField(blank=True, null=True)
    links_title = models.CharField(max_length=255, blank=True, null=True)
    msrp = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    msrp_display_actual_price_type = models.CharField(max_length=255, blank=True, null=True)
    msrp_enabled = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    news_from_date = models.DateTimeField(blank=True, null=True)
    news_to_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_type = models.IntegerField(blank=True, null=True)
    price_view = models.IntegerField(blank=True, null=True)
    recurring_profile = models.TextField(blank=True, null=True)
    required_options = models.SmallIntegerField()
    shipment_type = models.IntegerField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=64, blank=True, null=True)
    sku_type = models.IntegerField(blank=True, null=True)
    small_image = models.CharField(max_length=255, blank=True, null=True)
    small_image_label = models.CharField(max_length=255, blank=True, null=True)
    special_from_date = models.DateTimeField(blank=True, null=True)
    special_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    special_to_date = models.DateTimeField(blank=True, null=True)
    tax_class_id = models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_label = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    url_key = models.CharField(max_length=255, blank=True, null=True)
    url_path = models.CharField(max_length=255, blank=True, null=True)
    visibility = models.SmallIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weight_type = models.IntegerField(blank=True, null=True)
    auteur = models.CharField(max_length=255, blank=True, null=True)
    gewichtsklasse = models.IntegerField(blank=True, null=True)
    gewichtsklasse_value = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    am_shipping_type = models.IntegerField(blank=True, null=True)
    am_shipping_type_value = models.CharField(max_length=255, blank=True, null=True)
    merk = models.IntegerField(blank=True, null=True)
    merk_value = models.CharField(max_length=255, blank=True, null=True)
    smaak = models.CharField(max_length=255, blank=True, null=True)
    gewicht_nonfrozen = models.CharField(max_length=255, blank=True, null=True)
    type_vlees = models.CharField(max_length=255, blank=True, null=True)
    geschikt = models.CharField(max_length=255, blank=True, null=True)
    werkingsgebied = models.CharField(max_length=255, blank=True, null=True)
    geschiktmenu = models.SmallIntegerField(blank=True, null=True)
    verpakt_per = models.CharField(max_length=255, blank=True, null=True)
    shelf = models.CharField(max_length=255, blank=True, null=True)
    promo = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    smaak_site = models.CharField(max_length=255, blank=True, null=True)
    menutype_dieet = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_flat_1'


class CatalogProductIndexEav(models.Model):
    entity = models.ForeignKey(CatalogProductEntity)
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav'
        unique_together = (('entity_id', 'attribute_id', 'store_id', 'value'),)


class CatalogProductIndexEavDecimal(models.Model):
    entity = models.ForeignKey(CatalogProductEntity)
    attribute = models.ForeignKey('EavAttribute')
    store = models.ForeignKey('CoreStore')
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_decimal'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class CatalogProductIndexEavDecimalIdx(models.Model):
    entity_id = models.IntegerField()
    attribute_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_decimal_idx'
        unique_together = (('entity_id', 'attribute_id', 'store_id', 'value'),)


class CatalogProductIndexEavDecimalTmp(models.Model):
    entity_id = models.IntegerField()
    attribute_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_decimal_tmp'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class CatalogProductIndexEavIdx(models.Model):
    entity_id = models.IntegerField()
    attribute_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_idx'
        unique_together = (('entity_id', 'attribute_id', 'store_id', 'value'),)


class CatalogProductIndexEavTmp(models.Model):
    entity_id = models.IntegerField()
    attribute_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_tmp'
        unique_together = (('entity_id', 'attribute_id', 'store_id', 'value'),)


class CatalogProductIndexGroupPrice(models.Model):
    entity = models.ForeignKey(CatalogProductEntity)
    customer_group = models.ForeignKey('CustomerGroup')
    website = models.ForeignKey('CoreWebsite')
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_group_price'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPrice(models.Model):
    entity = models.ForeignKey(CatalogProductEntity)
    customer_group = models.ForeignKey('CustomerGroup')
    website = models.ForeignKey('CoreWebsite')
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    final_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceBundleIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price_type = models.SmallIntegerField()
    special_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tier = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceBundleOptIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_opt_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id'),)


class CatalogProductIndexPriceBundleOptTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_opt_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id'),)


class CatalogProductIndexPriceBundleSelIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    selection_id = models.IntegerField()
    group_type = models.SmallIntegerField(blank=True, null=True)
    is_required = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_sel_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id', 'selection_id'),)


class CatalogProductIndexPriceBundleSelTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    selection_id = models.IntegerField()
    group_type = models.SmallIntegerField(blank=True, null=True)
    is_required = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_sel_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id', 'selection_id'),)


class CatalogProductIndexPriceBundleTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price_type = models.SmallIntegerField()
    special_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tier = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceCfgOptAgrIdx(models.Model):
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_cfg_opt_agr_idx'
        unique_together = (('parent_id', 'child_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceCfgOptAgrTmp(models.Model):
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_cfg_opt_agr_tmp'
        unique_together = (('parent_id', 'child_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceCfgOptIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_cfg_opt_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceCfgOptTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_cfg_opt_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceDownlodIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4)
    max_price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_downlod_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceDownlodTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4)
    max_price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_downlod_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceFinalIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    orig_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tier = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_final_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceFinalTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    orig_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tier = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_final_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    final_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceOptAgrIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_opt_agr_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id'),)


class CatalogProductIndexPriceOptAgrTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_opt_agr_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id'),)


class CatalogProductIndexPriceOptIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_opt_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceOptTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_opt_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    final_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexTierPrice(models.Model):
    entity = models.ForeignKey(CatalogProductEntity)
    customer_group = models.ForeignKey('CustomerGroup')
    website = models.ForeignKey('CoreWebsite')
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_tier_price'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexWebsite(models.Model):
    website = models.ForeignKey('CoreWebsite', primary_key=True)
    website_date = models.DateField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_website'


class CatalogProductLink(models.Model):
    link_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity)
    linked_product = models.ForeignKey(CatalogProductEntity)
    link_type = models.ForeignKey('CatalogProductLinkType')

    class Meta:
        managed = False
        db_table = 'catalog_product_link'
        unique_together = (('link_type_id', 'product_id', 'linked_product_id'),)


class CatalogProductLinkAttribute(models.Model):
    product_link_attribute_id = models.SmallIntegerField(primary_key=True)
    link_type = models.ForeignKey('CatalogProductLinkType')
    product_link_attribute_code = models.CharField(max_length=32, blank=True, null=True)
    data_type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_link_attribute'


class CatalogProductLinkAttributeDecimal(models.Model):
    value_id = models.AutoField(primary_key=True)
    product_link_attribute = models.ForeignKey(CatalogProductLinkAttribute, blank=True, null=True)
    link = models.ForeignKey(CatalogProductLink)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_link_attribute_decimal'
        unique_together = (('product_link_attribute_id', 'link_id'),)


class CatalogProductLinkAttributeInt(models.Model):
    value_id = models.AutoField(primary_key=True)
    product_link_attribute = models.ForeignKey(CatalogProductLinkAttribute, blank=True, null=True)
    link = models.ForeignKey(CatalogProductLink)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_link_attribute_int'
        unique_together = (('product_link_attribute_id', 'link_id'),)


class CatalogProductLinkAttributeVarchar(models.Model):
    value_id = models.AutoField(primary_key=True)
    product_link_attribute = models.ForeignKey(CatalogProductLinkAttribute)
    link = models.ForeignKey(CatalogProductLink)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_link_attribute_varchar'
        unique_together = (('product_link_attribute_id', 'link_id'),)


class CatalogProductLinkType(models.Model):
    link_type_id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_link_type'


class CatalogProductOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity)
    type = models.CharField(max_length=50, blank=True, null=True)
    is_require = models.SmallIntegerField()
    sku = models.CharField(max_length=64, blank=True, null=True)
    max_characters = models.IntegerField(blank=True, null=True)
    file_extension = models.CharField(max_length=50, blank=True, null=True)
    image_size_x = models.SmallIntegerField(blank=True, null=True)
    image_size_y = models.SmallIntegerField(blank=True, null=True)
    sort_order = models.IntegerField()
    customoptions_is_onetime = models.IntegerField()
    image_path = models.CharField(max_length=255, blank=True, null=True)
    customer_groups = models.CharField(max_length=255, blank=True, null=True)
    qnty_input = models.IntegerField()
    in_group_id = models.IntegerField()
    is_dependent = models.IntegerField()
    div_class = models.CharField(max_length=64)
    sku_policy = models.IntegerField()
    image_mode = models.IntegerField()
    exclude_first_image = models.IntegerField()
    store_views = models.CharField(max_length=255, blank=True, null=True)
    show_swatch_title = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_option'


class CatalogProductOptionPrice(models.Model):
    option_price_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption)
    store = models.ForeignKey('CoreStore')
    price = models.DecimalField(max_digits=12, decimal_places=4)
    price_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_price'
        unique_together = (('option_id', 'store_id'),)


class CatalogProductOptionTitle(models.Model):
    option_title_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption)
    store = models.ForeignKey('CoreStore')
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_title'
        unique_together = (('option_id', 'store_id'),)


class CatalogProductOptionTypePrice(models.Model):
    option_type_price_id = models.AutoField(primary_key=True)
    option_type = models.ForeignKey('CatalogProductOptionTypeValue')
    store = models.ForeignKey('CoreStore')
    price = models.DecimalField(max_digits=12, decimal_places=4)
    price_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_type_price'
        unique_together = (('option_type_id', 'store_id'),)


class CatalogProductOptionTypeTitle(models.Model):
    option_type_title_id = models.AutoField(primary_key=True)
    option_type = models.ForeignKey('CatalogProductOptionTypeValue')
    store = models.ForeignKey('CoreStore')
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_type_title'
        unique_together = (('option_type_id', 'store_id'),)


class CatalogProductOptionTypeValue(models.Model):
    option_type_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption)
    sku = models.CharField(max_length=64, blank=True, null=True)
    sort_order = models.IntegerField()
    customoptions_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    default = models.IntegerField()
    in_group_id = models.IntegerField()
    dependent_ids = models.TextField()
    weight = models.DecimalField(max_digits=12, decimal_places=4)
    cost = models.DecimalField(max_digits=12, decimal_places=4)
    extra = models.CharField(max_length=10)
    customoptions_min_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    customoptions_max_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    descr = models.CharField(max_length=255, blank=True, null=True)
    upc = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_type_value'


class CatalogProductRelation(models.Model):
    parent = models.ForeignKey(CatalogProductEntity)
    child = models.ForeignKey(CatalogProductEntity)

    class Meta:
        managed = False
        db_table = 'catalog_product_relation'
        unique_together = (('parent_id', 'child_id'),)


class CatalogProductSuperAttribute(models.Model):
    product_super_attribute_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity)
    attribute_id = models.SmallIntegerField()
    position = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_super_attribute'
        unique_together = (('product_id', 'attribute_id'),)


class CatalogProductSuperAttributeDefaultValue(models.Model):
    value_id = models.AutoField(primary_key=True)
    product_super_attribute = models.ForeignKey(CatalogProductSuperAttribute)
    store = models.ForeignKey('CoreStore', blank=True, null=True)
    value_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_super_attribute_default_value'


class CatalogProductSuperAttributeLabel(models.Model):
    value_id = models.AutoField(primary_key=True)
    product_super_attribute = models.ForeignKey(CatalogProductSuperAttribute)
    store = models.ForeignKey('CoreStore')
    use_default = models.SmallIntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_super_attribute_label'
        unique_together = (('product_super_attribute_id', 'store_id'),)


class CatalogProductSuperAttributePricing(models.Model):
    value_id = models.AutoField(primary_key=True)
    product_super_attribute = models.ForeignKey(CatalogProductSuperAttribute)
    value_index = models.CharField(max_length=255, blank=True, null=True)
    is_percent = models.SmallIntegerField(blank=True, null=True)
    pricing_value = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    website = models.ForeignKey('CoreWebsite')

    class Meta:
        managed = False
        db_table = 'catalog_product_super_attribute_pricing'
        unique_together = (('product_super_attribute_id', 'value_index', 'website_id'),)


class CatalogProductSuperLink(models.Model):
    link_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity)
    parent = models.ForeignKey(CatalogProductEntity)

    class Meta:
        managed = False
        db_table = 'catalog_product_super_link'
        unique_together = (('product_id', 'parent_id'),)


class CatalogProductWebsite(models.Model):
    product = models.ForeignKey(CatalogProductEntity)
    website = models.ForeignKey('CoreWebsite')

    class Meta:
        managed = False
        db_table = 'catalog_product_website'
        unique_together = (('product_id', 'website_id'),)


class CataloginventoryStock(models.Model):
    stock_id = models.SmallIntegerField(primary_key=True)
    stock_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock'


class CataloginventoryStockItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity)
    stock = models.ForeignKey(CataloginventoryStock)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    min_qty = models.DecimalField(max_digits=12, decimal_places=4)
    use_config_min_qty = models.SmallIntegerField()
    is_qty_decimal = models.SmallIntegerField()
    backorders = models.SmallIntegerField()
    use_config_backorders = models.SmallIntegerField()
    min_sale_qty = models.DecimalField(max_digits=12, decimal_places=4)
    use_config_min_sale_qty = models.SmallIntegerField()
    max_sale_qty = models.DecimalField(max_digits=12, decimal_places=4)
    use_config_max_sale_qty = models.SmallIntegerField()
    is_in_stock = models.SmallIntegerField()
    low_stock_date = models.DateTimeField(blank=True, null=True)
    notify_stock_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    use_config_notify_stock_qty = models.SmallIntegerField()
    manage_stock = models.SmallIntegerField()
    use_config_manage_stock = models.SmallIntegerField()
    stock_status_changed_auto = models.SmallIntegerField()
    use_config_qty_increments = models.SmallIntegerField()
    qty_increments = models.DecimalField(max_digits=12, decimal_places=4)
    use_config_enable_qty_inc = models.SmallIntegerField()
    enable_qty_increments = models.SmallIntegerField()
    is_decimal_divided = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock_item'
        unique_together = (('product_id', 'stock_id'),)


class CataloginventoryStockStatus(models.Model):
    product = models.ForeignKey(CatalogProductEntity)
    website = models.ForeignKey('CoreWebsite')
    stock = models.ForeignKey(CataloginventoryStock)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    stock_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock_status'
        unique_together = (('product_id', 'website_id', 'stock_id'),)


class CataloginventoryStockStatusIdx(models.Model):
    product_id = models.IntegerField()
    website_id = models.SmallIntegerField()
    stock_id = models.SmallIntegerField()
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    stock_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock_status_idx'
        unique_together = (('product_id', 'website_id', 'stock_id'),)


class CataloginventoryStockStatusTmp(models.Model):
    product_id = models.IntegerField()
    website_id = models.SmallIntegerField()
    stock_id = models.SmallIntegerField()
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    stock_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock_status_tmp'
        unique_together = (('product_id', 'website_id', 'stock_id'),)


class Catalogrule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)
    stop_rules_processing = models.SmallIntegerField()
    sort_order = models.IntegerField()
    simple_action = models.CharField(max_length=32, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    sub_is_enable = models.SmallIntegerField()
    sub_simple_action = models.CharField(max_length=32, blank=True, null=True)
    sub_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalogrule'


class CatalogruleAffectedProduct(models.Model):
    product_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'catalogrule_affected_product'


class CatalogruleCustomerGroup(models.Model):
    rule = models.ForeignKey(Catalogrule)
    customer_group = models.ForeignKey('CustomerGroup')

    class Meta:
        managed = False
        db_table = 'catalogrule_customer_group'
        unique_together = (('rule_id', 'customer_group_id'),)


class CatalogruleGroupWebsite(models.Model):
    rule = models.ForeignKey(Catalogrule)
    customer_group = models.ForeignKey('CustomerGroup')
    website = models.ForeignKey('CoreWebsite')

    class Meta:
        managed = False
        db_table = 'catalogrule_group_website'
        unique_together = (('rule_id', 'customer_group_id', 'website_id'),)


class CatalogruleProduct(models.Model):
    rule_product_id = models.AutoField(primary_key=True)
    rule = models.ForeignKey(Catalogrule)
    from_time = models.IntegerField()
    to_time = models.IntegerField()
    customer_group = models.ForeignKey('CustomerGroup')
    product = models.ForeignKey(CatalogProductEntity)
    action_operator = models.CharField(max_length=10, blank=True, null=True)
    action_amount = models.DecimalField(max_digits=12, decimal_places=4)
    action_stop = models.SmallIntegerField()
    sort_order = models.IntegerField()
    website = models.ForeignKey('CoreWebsite')
    sub_simple_action = models.CharField(max_length=32, blank=True, null=True)
    sub_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalogrule_product'
        unique_together = (('rule_id', 'from_time', 'to_time', 'website_id', 'customer_group_id', 'product_id', 'sort_order'),)


class CatalogruleProductPrice(models.Model):
    rule_product_price_id = models.AutoField(primary_key=True)
    rule_date = models.DateField()
    customer_group = models.ForeignKey('CustomerGroup')
    product = models.ForeignKey(CatalogProductEntity)
    rule_price = models.DecimalField(max_digits=12, decimal_places=4)
    website = models.ForeignKey('CoreWebsite')
    latest_start_date = models.DateField(blank=True, null=True)
    earliest_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogrule_product_price'
        unique_together = (('rule_date', 'website_id', 'customer_group_id', 'product_id'),)


class CatalogruleWebsite(models.Model):
    rule = models.ForeignKey(Catalogrule)
    website = models.ForeignKey('CoreWebsite')

    class Meta:
        managed = False
        db_table = 'catalogrule_website'
        unique_together = (('rule_id', 'website_id'),)


class CatalogsearchFulltext(models.Model):
    fulltext_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    store_id = models.SmallIntegerField()
    data_index = models.TextField(blank=True, null=True)
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    merk = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    extrainformatie = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogsearch_fulltext'
        unique_together = (('product_id', 'store_id'),)


class CatalogsearchQuery(models.Model):
    query_id = models.AutoField(primary_key=True)
    query_text = models.CharField(max_length=255, blank=True, null=True)
    num_results = models.IntegerField()
    popularity = models.IntegerField()
    redirect = models.CharField(max_length=255, blank=True, null=True)
    synonym_for = models.CharField(max_length=255, blank=True, null=True)
    store = models.ForeignKey('CoreStore')
    display_in_terms = models.SmallIntegerField()
    is_active = models.SmallIntegerField(blank=True, null=True)
    is_processed = models.SmallIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'catalogsearch_query'


class CatalogsearchResult(models.Model):
    query = models.ForeignKey(CatalogsearchQuery)
    product = models.ForeignKey(CatalogProductEntity)
    relevance = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalogsearch_result'
        unique_together = (('query_id', 'product_id'),)


class CheckoutAgreement(models.Model):
    agreement_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_height = models.CharField(max_length=25, blank=True, null=True)
    checkbox_text = models.TextField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    is_html = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'checkout_agreement'


class CheckoutAgreementStore(models.Model):
    agreement = models.ForeignKey(CheckoutAgreement)
    store = models.ForeignKey('CoreStore')

    class Meta:
        managed = False
        db_table = 'checkout_agreement_store'
        unique_together = (('agreement_id', 'store_id'),)


class Checkoutrule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    uses_per_customer = models.IntegerField()
    customer_group_ids = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    conditions_serialized = models.TextField()
    actions_serialized = models.TextField()
    stop_rules_processing = models.IntegerField()
    is_advanced = models.IntegerField()
    product_ids = models.TextField(blank=True, null=True)
    sort_order = models.IntegerField()
    simple_action = models.CharField(max_length=32)
    payment_methods_ids = models.TextField()
    shipping_methods_ids = models.TextField()
    times_used = models.IntegerField()
    is_rss = models.IntegerField()
    website_ids = models.TextField(blank=True, null=True)
    coupon_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'checkoutrule'


class CheckoutruleLabel(models.Model):
    label_id = models.AutoField(primary_key=True)
    rule = models.ForeignKey(Checkoutrule)
    store = models.ForeignKey('CoreStore')
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkoutrule_label'
        unique_together = (('rule_id', 'store_id'),)


class CmsBlock(models.Model):
    block_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cms_block'


class CmsBlockStore(models.Model):
    block = models.ForeignKey(CmsBlock)
    store = models.ForeignKey('CoreStore')

    class Meta:
        managed = False
        db_table = 'cms_block_store'
        unique_together = (('block_id', 'store_id'),)


class CmsPage(models.Model):
    page_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    root_template = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    content_heading = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    sort_order = models.SmallIntegerField()
    layout_update_xml = models.TextField(blank=True, null=True)
    custom_theme = models.CharField(max_length=100, blank=True, null=True)
    custom_root_template = models.CharField(max_length=255, blank=True, null=True)
    custom_layout_update_xml = models.TextField(blank=True, null=True)
    custom_theme_from = models.DateField(blank=True, null=True)
    custom_theme_to = models.DateField(blank=True, null=True)
    alternate_group = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_page'


class CmsPageStore(models.Model):
    page = models.ForeignKey(CmsPage)
    store = models.ForeignKey('CoreStore')

    class Meta:
        managed = False
        db_table = 'cms_page_store'
        unique_together = (('page_id', 'store_id'),)


class CoreCache(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    data = models.TextField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    expire_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_cache'


class CoreCacheOption(models.Model):
    code = models.CharField(primary_key=True, max_length=32)
    value = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_cache_option'


class CoreCacheTag(models.Model):
    tag = models.CharField(max_length=100)
    cache_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'core_cache_tag'
        unique_together = (('tag', 'cache_id'),)


class CoreConfigData(models.Model):
    config_id = models.AutoField(primary_key=True)
    scope = models.CharField(max_length=8)
    scope_id = models.IntegerField()
    path = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_config_data'
        unique_together = (('scope', 'scope_id', 'path'),)


class CoreEmailQueue(models.Model):
    message_id = models.AutoField(primary_key=True)
    entity_id = models.IntegerField(blank=True, null=True)
    entity_type = models.CharField(max_length=128, blank=True, null=True)
    event_type = models.CharField(max_length=128, blank=True, null=True)
    message_body_hash = models.CharField(max_length=64)
    message_body = models.TextField()
    message_parameters = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    processed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_email_queue'


class CoreEmailQueueRecipients(models.Model):
    recipient_id = models.AutoField(primary_key=True)
    message = models.ForeignKey(CoreEmailQueue)
    recipient_email = models.CharField(max_length=128)
    recipient_name = models.CharField(max_length=255)
    email_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_email_queue_recipients'
        unique_together = (('message_id', 'recipient_email', 'email_type'),)


class CoreEmailTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    template_code = models.CharField(unique=True, max_length=150)
    template_text = models.TextField()
    template_styles = models.TextField(blank=True, null=True)
    template_type = models.IntegerField(blank=True, null=True)
    template_subject = models.CharField(max_length=200)
    template_sender_name = models.CharField(max_length=200, blank=True, null=True)
    template_sender_email = models.CharField(max_length=200, blank=True, null=True)
    added_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    orig_template_code = models.CharField(max_length=200, blank=True, null=True)
    orig_template_variables = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_email_template'


class CoreFlag(models.Model):
    flag_id = models.AutoField(primary_key=True)
    flag_code = models.CharField(max_length=255)
    state = models.SmallIntegerField()
    flag_data = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'core_flag'


class CoreLayoutLink(models.Model):
    layout_link_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('CoreStore')
    area = models.CharField(max_length=64, blank=True, null=True)
    package = models.CharField(max_length=64, blank=True, null=True)
    theme = models.CharField(max_length=64, blank=True, null=True)
    layout_update = models.ForeignKey('CoreLayoutUpdate')

    class Meta:
        managed = False
        db_table = 'core_layout_link'
        unique_together = (('store_id', 'package', 'theme', 'layout_update_id'),)


class CoreLayoutUpdate(models.Model):
    layout_update_id = models.AutoField(primary_key=True)
    handle = models.CharField(max_length=255, blank=True, null=True)
    xml = models.TextField(blank=True, null=True)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_layout_update'


class CoreResource(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    version = models.CharField(max_length=50, blank=True, null=True)
    data_version = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_resource'


class CoreSession(models.Model):
    session_id = models.CharField(primary_key=True, max_length=255)
    session_expires = models.IntegerField()
    session_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_session'


class CoreStore(models.Model):
    store_id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    website = models.ForeignKey('CoreWebsite')
    group = models.ForeignKey('CoreStoreGroup')
    name = models.CharField(max_length=255)
    sort_order = models.SmallIntegerField()
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_store'


class CoreStoreGroup(models.Model):
    group_id = models.SmallIntegerField(primary_key=True)
    website = models.ForeignKey('CoreWebsite')
    name = models.CharField(max_length=255)
    root_category_id = models.IntegerField()
    default_store_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_store_group'


class CoreTranslate(models.Model):
    key_id = models.AutoField(primary_key=True)
    string = models.CharField(max_length=255)
    store = models.ForeignKey(CoreStore)
    translate = models.CharField(max_length=255, blank=True, null=True)
    locale = models.CharField(max_length=20)
    crc_string = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'core_translate'
        unique_together = (('store_id', 'locale', 'crc_string', 'string'),)


class CoreUrlRewrite(models.Model):
    url_rewrite_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(CoreStore)
    id_path = models.CharField(max_length=255, blank=True, null=True)
    request_path = models.CharField(max_length=255, blank=True, null=True)
    target_path = models.CharField(max_length=255, blank=True, null=True)
    is_system = models.SmallIntegerField(blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(CatalogCategoryEntity, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_url_rewrite'
        unique_together = (('id_path', 'is_system', 'store_id'), ('request_path', 'store_id'),)


class CoreVariable(models.Model):
    variable_id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_variable'


class CoreVariableValue(models.Model):
    value_id = models.AutoField(primary_key=True)
    variable = models.ForeignKey(CoreVariable)
    store = models.ForeignKey(CoreStore)
    plain_value = models.TextField(blank=True, null=True)
    html_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_variable_value'
        unique_together = (('variable_id', 'store_id'),)


class CoreWebsite(models.Model):
    website_id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    sort_order = models.SmallIntegerField()
    default_group_id = models.SmallIntegerField()
    is_default = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_website'


class CouponAggregated(models.Model):
    period = models.DateField()
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_uses = models.IntegerField()
    subtotal_amount = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    rule_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_aggregated'
        unique_together = (('period', 'store_id', 'order_status', 'coupon_code'),)


class CouponAggregatedOrder(models.Model):
    period = models.DateField()
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_uses = models.IntegerField()
    subtotal_amount = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount = models.DecimalField(max_digits=12, decimal_places=4)
    rule_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_aggregated_order'
        unique_together = (('period', 'store_id', 'order_status', 'coupon_code'),)


class CouponAggregatedUpdated(models.Model):
    period = models.DateField()
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_uses = models.IntegerField()
    subtotal_amount = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    rule_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_aggregated_updated'
        unique_together = (('period', 'store_id', 'order_status', 'coupon_code'),)


class CronSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    job_code = models.CharField(max_length=255)
    status = models.CharField(max_length=7)
    messages = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    scheduled_at = models.DateTimeField(blank=True, null=True)
    executed_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    pid = models.CharField(max_length=255, blank=True, null=True)
    progress_message = models.TextField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)
    kill_request = models.DateTimeField(blank=True, null=True)
    scheduled_by = models.IntegerField(blank=True, null=True)
    scheduled_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cron_schedule'


class CustomerAddressEntity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute_set_id = models.SmallIntegerField()
    increment_id = models.CharField(max_length=50, blank=True, null=True)
    parent = models.ForeignKey('CustomerEntity', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'customer_address_entity'


class CustomerAddressEntityDatetime(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerAddressEntity)
    value = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_address_entity_datetime'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerAddressEntityDecimal(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerAddressEntity)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'customer_address_entity_decimal'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerAddressEntityInt(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerAddressEntity)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_address_entity_int'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerAddressEntityText(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerAddressEntity)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer_address_entity_text'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerAddressEntityVarchar(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerAddressEntity)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_address_entity_varchar'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerEavAttribute(models.Model):
    attribute = models.ForeignKey('EavAttribute', primary_key=True)
    is_visible = models.SmallIntegerField()
    input_filter = models.CharField(max_length=255, blank=True, null=True)
    multiline_count = models.SmallIntegerField()
    validate_rules = models.TextField(blank=True, null=True)
    is_system = models.SmallIntegerField()
    sort_order = models.IntegerField()
    data_model = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_eav_attribute'


class CustomerEavAttributeWebsite(models.Model):
    attribute = models.ForeignKey('EavAttribute')
    website = models.ForeignKey(CoreWebsite)
    is_visible = models.SmallIntegerField(blank=True, null=True)
    is_required = models.SmallIntegerField(blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    multiline_count = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_eav_attribute_website'
        unique_together = (('attribute_id', 'website_id'),)


class CustomerEntity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute_set_id = models.SmallIntegerField()
    website = models.ForeignKey(CoreWebsite, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.SmallIntegerField()
    increment_id = models.CharField(max_length=50, blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.SmallIntegerField()
    disable_auto_group_change = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'customer_entity'
        unique_together = (('email', 'website_id'),)


class CustomerEntityDatetime(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerEntity)
    value = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_entity_datetime'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerEntityDecimal(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerEntity)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'customer_entity_decimal'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerEntityInt(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerEntity)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_entity_int'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerEntityText(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerEntity)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer_entity_text'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerEntityVarchar(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute = models.ForeignKey('EavAttribute')
    entity = models.ForeignKey(CustomerEntity)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_entity_varchar'
        unique_together = (('entity_id', 'attribute_id'),)


class CustomerFormAttribute(models.Model):
    form_code = models.CharField(max_length=32)
    attribute = models.ForeignKey('EavAttribute')

    class Meta:
        managed = False
        db_table = 'customer_form_attribute'
        unique_together = (('form_code', 'attribute_id'),)


class CustomerGroup(models.Model):
    customer_group_id = models.SmallIntegerField(primary_key=True)
    customer_group_code = models.CharField(max_length=32)
    tax_class_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_group'


class CustomgridGrid(models.Model):
    grid_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    module_name = models.CharField(max_length=255)
    controller_name = models.CharField(max_length=255)
    block_type = models.CharField(max_length=255)
    rewriting_class_name = models.CharField(max_length=255, blank=True, null=True)
    block_id = models.CharField(max_length=255, blank=True, null=True)
    max_attribute_column_id = models.IntegerField()
    max_custom_column_id = models.IntegerField()
    default_page = models.IntegerField(blank=True, null=True)
    default_limit = models.IntegerField(blank=True, null=True)
    default_sort = models.CharField(max_length=255, blank=True, null=True)
    default_dir = models.CharField(max_length=4, blank=True, null=True)
    default_filter = models.TextField(blank=True, null=True)
    disabled = models.IntegerField()
    default_page_behaviour = models.CharField(max_length=14, blank=True, null=True)
    default_limit_behaviour = models.CharField(max_length=14, blank=True, null=True)
    default_sort_behaviour = models.CharField(max_length=14, blank=True, null=True)
    default_dir_behaviour = models.CharField(max_length=14, blank=True, null=True)
    default_filter_behaviour = models.CharField(max_length=17, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customgrid_grid'


class CustomgridGridColumn(models.Model):
    column_id = models.AutoField(primary_key=True)
    grid = models.ForeignKey(CustomgridGrid)
    id = models.CharField(max_length=255)
    index = models.CharField(max_length=255, blank=True, null=True)
    width = models.CharField(max_length=128, blank=True, null=True)
    align = models.CharField(max_length=6, blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField()
    origin = models.CharField(max_length=10)
    is_visible = models.IntegerField()
    is_system = models.IntegerField()
    missing = models.IntegerField()
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    renderer_type = models.CharField(max_length=255, blank=True, null=True)
    renderer_params = models.TextField(blank=True, null=True)
    allow_edit = models.IntegerField()
    profile = models.ForeignKey('CustomgridGridProfile', blank=True, null=True)
    custom_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customgrid_grid_column'


class CustomgridGridProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    grid = models.ForeignKey(CustomgridGrid)
    name = models.CharField(max_length=255)
    default_page = models.IntegerField(blank=True, null=True)
    default_limit = models.IntegerField(blank=True, null=True)
    default_sort = models.CharField(max_length=255, blank=True, null=True)
    default_direction = models.CharField(max_length=4, blank=True, null=True)
    default_filters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customgrid_grid_profile'


class CustomgridGridRole(models.Model):
    grid_role_id = models.AutoField(primary_key=True)
    grid = models.ForeignKey(CustomgridGrid)
    role = models.ForeignKey(AdminRole)
    permissions = models.TextField(blank=True, null=True)
    default_profile = models.ForeignKey(CustomgridGridProfile, blank=True, null=True)
    available_profiles = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customgrid_grid_role'


class CustomgridGridUser(models.Model):
    grid_user_id = models.AutoField(primary_key=True)
    grid = models.ForeignKey(CustomgridGrid)
    user = models.ForeignKey(AdminUser)
    default_profile = models.ForeignKey(CustomgridGridProfile, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customgrid_grid_user'


class CustomgridOptionsSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'customgrid_options_source'


class CustomgridOptionsSourceModel(models.Model):
    model_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(CustomgridOptionsSource)
    model_name = models.CharField(max_length=255)
    model_type = models.CharField(max_length=14)
    method = models.CharField(max_length=255)
    return_type = models.CharField(max_length=13)
    value_key = models.CharField(max_length=255, blank=True, null=True)
    label_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customgrid_options_source_model'


class CustomgridOptionsSourceOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(CustomgridOptionsSource)
    value = models.CharField(max_length=255)
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customgrid_options_source_option'


class DataflowBatch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey('DataflowProfile')
    store = models.ForeignKey(CoreStore)
    adapter = models.CharField(max_length=128, blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataflow_batch'


class DataflowBatchExport(models.Model):
    batch_export_id = models.BigIntegerField(primary_key=True)
    batch = models.ForeignKey(DataflowBatch)
    batch_data = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'dataflow_batch_export'


class DataflowBatchImport(models.Model):
    batch_import_id = models.BigIntegerField(primary_key=True)
    batch = models.ForeignKey(DataflowBatch)
    batch_data = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'dataflow_batch_import'


class DataflowImportData(models.Model):
    import_id = models.AutoField(primary_key=True)
    session = models.ForeignKey('DataflowSession', blank=True, null=True)
    serial_number = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dataflow_import_data'


class DataflowProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    actions_xml = models.TextField(blank=True, null=True)
    gui_data = models.TextField(blank=True, null=True)
    direction = models.CharField(max_length=6, blank=True, null=True)
    entity_type = models.CharField(max_length=64, blank=True, null=True)
    store_id = models.SmallIntegerField()
    data_transfer = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataflow_profile'


class DataflowProfileHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(DataflowProfile)
    action_code = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.IntegerField()
    performed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataflow_profile_history'


class DataflowSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    direction = models.CharField(max_length=32, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataflow_session'


class DesignChange(models.Model):
    design_change_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(CoreStore)
    design = models.CharField(max_length=255, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_change'


class DirectoryCountry(models.Model):
    country_id = models.CharField(primary_key=True, max_length=2)
    iso2_code = models.CharField(max_length=2, blank=True, null=True)
    iso3_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directory_country'


class DirectoryCountryFormat(models.Model):
    country_format_id = models.AutoField(primary_key=True)
    country_id = models.CharField(max_length=2, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    format = models.TextField()

    class Meta:
        managed = False
        db_table = 'directory_country_format'
        unique_together = (('country_id', 'type'),)


class DirectoryCountryRegion(models.Model):
    region_id = models.AutoField(primary_key=True)
    country_id = models.CharField(max_length=4)
    code = models.CharField(max_length=32, blank=True, null=True)
    default_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directory_country_region'


class DirectoryCountryRegionName(models.Model):
    locale = models.CharField(max_length=8)
    region = models.ForeignKey(DirectoryCountryRegion)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directory_country_region_name'
        unique_together = (('locale', 'region_id'),)


class DirectoryCurrencyRate(models.Model):
    currency_from = models.CharField(max_length=3)
    currency_to = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=24, decimal_places=12)

    class Meta:
        managed = False
        db_table = 'directory_currency_rate'
        unique_together = (('currency_from', 'currency_to'),)


class DownloadableLink(models.Model):
    link_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity)
    sort_order = models.IntegerField()
    number_of_downloads = models.IntegerField(blank=True, null=True)
    is_shareable = models.SmallIntegerField()
    link_url = models.CharField(max_length=255, blank=True, null=True)
    link_file = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=20, blank=True, null=True)
    sample_url = models.CharField(max_length=255, blank=True, null=True)
    sample_file = models.CharField(max_length=255, blank=True, null=True)
    sample_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadable_link'


class DownloadableLinkPrice(models.Model):
    price_id = models.AutoField(primary_key=True)
    link = models.ForeignKey(DownloadableLink)
    website = models.ForeignKey(CoreWebsite)
    price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'downloadable_link_price'


class DownloadableLinkPurchased(models.Model):
    purchased_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('SalesFlatOrder', blank=True, null=True)
    order_increment_id = models.CharField(max_length=50, blank=True, null=True)
    order_item_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_sku = models.CharField(max_length=255, blank=True, null=True)
    link_section_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadable_link_purchased'


class DownloadableLinkPurchasedItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    purchased = models.ForeignKey(DownloadableLinkPurchased)
    order_item = models.ForeignKey('SalesFlatOrderItem', blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    link_hash = models.CharField(max_length=255, blank=True, null=True)
    number_of_downloads_bought = models.IntegerField()
    number_of_downloads_used = models.IntegerField()
    link_id = models.IntegerField()
    link_title = models.CharField(max_length=255, blank=True, null=True)
    is_shareable = models.SmallIntegerField()
    link_url = models.CharField(max_length=255, blank=True, null=True)
    link_file = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'downloadable_link_purchased_item'


class DownloadableLinkTitle(models.Model):
    title_id = models.AutoField(primary_key=True)
    link = models.ForeignKey(DownloadableLink)
    store = models.ForeignKey(CoreStore)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadable_link_title'
        unique_together = (('link_id', 'store_id'),)


class DownloadableSample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity)
    sample_url = models.CharField(max_length=255, blank=True, null=True)
    sample_file = models.CharField(max_length=255, blank=True, null=True)
    sample_type = models.CharField(max_length=20, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'downloadable_sample'


class DownloadableSampleTitle(models.Model):
    title_id = models.AutoField(primary_key=True)
    sample = models.ForeignKey(DownloadableSample)
    store = models.ForeignKey(CoreStore)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadable_sample_title'
        unique_together = (('sample_id', 'store_id'),)


class EavAttribute(models.Model):
    attribute_id = models.SmallIntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute_code = models.CharField(max_length=255, blank=True, null=True)
    attribute_model = models.CharField(max_length=255, blank=True, null=True)
    backend_model = models.CharField(max_length=255, blank=True, null=True)
    backend_type = models.CharField(max_length=8)
    backend_table = models.CharField(max_length=255, blank=True, null=True)
    frontend_model = models.CharField(max_length=255, blank=True, null=True)
    frontend_input = models.CharField(max_length=50, blank=True, null=True)
    frontend_label = models.CharField(max_length=255, blank=True, null=True)
    frontend_class = models.CharField(max_length=255, blank=True, null=True)
    source_model = models.CharField(max_length=255, blank=True, null=True)
    is_required = models.SmallIntegerField()
    is_user_defined = models.SmallIntegerField()
    default_value = models.TextField(blank=True, null=True)
    is_unique = models.SmallIntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_attribute'
        unique_together = (('entity_type_id', 'attribute_code'),)


class EavAttributeGroup(models.Model):
    attribute_group_id = models.SmallIntegerField(primary_key=True)
    attribute_set = models.ForeignKey('EavAttributeSet')
    attribute_group_name = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.SmallIntegerField()
    default_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_attribute_group'
        unique_together = (('attribute_set_id', 'attribute_group_name'),)


class EavAttributeLabel(models.Model):
    attribute_label_id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(EavAttribute)
    store = models.ForeignKey(CoreStore)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_attribute_label'


class EavAttributeOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(EavAttribute)
    sort_order = models.SmallIntegerField()
    image = models.TextField()
    thumb = models.TextField()

    class Meta:
        managed = False
        db_table = 'eav_attribute_option'


class EavAttributeOptionValue(models.Model):
    value_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(EavAttributeOption)
    store = models.ForeignKey(CoreStore)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_attribute_option_value'


class EavAttributeSet(models.Model):
    attribute_set_id = models.SmallIntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute_set_name = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_attribute_set'
        unique_together = (('entity_type_id', 'attribute_set_name'),)


class EavEntity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute_set_id = models.SmallIntegerField()
    increment_id = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.IntegerField()
    store = models.ForeignKey(CoreStore)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_entity'


class EavEntityAttribute(models.Model):
    entity_attribute_id = models.AutoField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute_set_id = models.SmallIntegerField()
    attribute_group = models.ForeignKey(EavAttributeGroup)
    attribute = models.ForeignKey(EavAttribute)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_entity_attribute'
        unique_together = (('attribute_group_id', 'attribute_id'), ('attribute_set_id', 'attribute_id'),)


class EavEntityDatetime(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore)
    entity = models.ForeignKey(EavEntity)
    value = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eav_entity_datetime'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class EavEntityDecimal(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore)
    entity = models.ForeignKey(EavEntity)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'eav_entity_decimal'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class EavEntityInt(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore)
    entity = models.ForeignKey(EavEntity)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eav_entity_int'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class EavEntityStore(models.Model):
    entity_store_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    store = models.ForeignKey(CoreStore)
    increment_prefix = models.CharField(max_length=20, blank=True, null=True)
    increment_last_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_entity_store'


class EavEntityText(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType')
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore)
    entity = models.ForeignKey(EavEntity)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'eav_entity_text'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class EavEntityType(models.Model):
    entity_type_id = models.SmallIntegerField(primary_key=True)
    entity_type_code = models.CharField(max_length=50)
    entity_model = models.CharField(max_length=255)
    attribute_model = models.CharField(max_length=255, blank=True, null=True)
    entity_table = models.CharField(max_length=255, blank=True, null=True)
    value_table_prefix = models.CharField(max_length=255, blank=True, null=True)
    entity_id_field = models.CharField(max_length=255, blank=True, null=True)
    is_data_sharing = models.SmallIntegerField()
    data_sharing_key = models.CharField(max_length=100, blank=True, null=True)
    default_attribute_set_id = models.SmallIntegerField()
    increment_model = models.CharField(max_length=255, blank=True, null=True)
    increment_per_store = models.SmallIntegerField()
    increment_pad_length = models.SmallIntegerField()
    increment_pad_char = models.CharField(max_length=1)
    additional_attribute_table = models.CharField(max_length=255, blank=True, null=True)
    entity_attribute_collection = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_entity_type'


class EavEntityVarchar(models.Model):
    value_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey(EavEntityType)
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore)
    entity = models.ForeignKey(EavEntity)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_entity_varchar'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class EavFormElement(models.Model):
    element_id = models.AutoField(primary_key=True)
    type = models.ForeignKey('EavFormType')
    fieldset = models.ForeignKey('EavFormFieldset', blank=True, null=True)
    attribute = models.ForeignKey(EavAttribute)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eav_form_element'
        unique_together = (('type_id', 'attribute_id'),)


class EavFormFieldset(models.Model):
    fieldset_id = models.SmallIntegerField(primary_key=True)
    type = models.ForeignKey('EavFormType')
    code = models.CharField(max_length=64)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eav_form_fieldset'
        unique_together = (('type_id', 'code'),)


class EavFormFieldsetLabel(models.Model):
    fieldset = models.ForeignKey(EavFormFieldset)
    store = models.ForeignKey(CoreStore)
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'eav_form_fieldset_label'
        unique_together = (('fieldset_id', 'store_id'),)


class EavFormType(models.Model):
    type_id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(max_length=64)
    label = models.CharField(max_length=255)
    is_system = models.SmallIntegerField()
    theme = models.CharField(max_length=64, blank=True, null=True)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'eav_form_type'
        unique_together = (('code', 'theme', 'store_id'),)


class EavFormTypeEntity(models.Model):
    type = models.ForeignKey(EavFormType)
    entity_type = models.ForeignKey(EavEntityType)

    class Meta:
        managed = False
        db_table = 'eav_form_type_entity'
        unique_together = (('type_id', 'entity_type_id'),)


class EbizmartsAbandonedcartAbtesting(models.Model):
    updated_at = models.DateTimeField()
    current_status = models.SmallIntegerField(blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebizmarts_abandonedcart_abtesting'


class EbizmartsAbandonedcartPopup(models.Model):
    email = models.CharField(max_length=128, blank=True, null=True)
    updated_at = models.DateTimeField()
    counter = models.IntegerField(blank=True, null=True)
    processed = models.SmallIntegerField(blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebizmarts_abandonedcart_popup'


class EbizmartsAutoresponderBacktostock(models.Model):
    backtostock_id = models.AutoField(primary_key=True)
    alert_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ebizmarts_autoresponder_backtostock'


class EbizmartsAutoresponderBacktostockAlert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ebizmarts_autoresponder_backtostock_alert'


class EbizmartsAutoresponderReview(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)
    items = models.SmallIntegerField(blank=True, null=True)
    counter = models.SmallIntegerField(blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ebizmarts_autoresponder_review'


class EbizmartsAutoresponderUnsubscribe(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    list = models.CharField(max_length=255, blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)
    unsubscribed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ebizmarts_autoresponder_unsubscribe'


class EbizmartsAutoresponderVisited(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)
    visited_at = models.DateTimeField()
    customer_email = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebizmarts_autoresponder_visited'


class ExtensionConflict(models.Model):
    ec_id = models.AutoField(primary_key=True)
    ec_core_module = models.CharField(max_length=255)
    ec_core_class = models.CharField(max_length=255)
    ec_rewrite_classes = models.TextField()
    ec_is_conflict = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'extension_conflict'


class GiftMessage(models.Model):
    gift_message_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    sender = models.CharField(max_length=255, blank=True, null=True)
    recipient = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gift_message'


class GooglecheckoutNotification(models.Model):
    serial_number = models.CharField(primary_key=True, max_length=64)
    started_at = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'googlecheckout_notification'


class Imageoption(models.Model):
    imageoption_id = models.AutoField(primary_key=True)
    option_type = models.ForeignKey(CatalogProductOptionTypeValue)
    option = models.ForeignKey(CatalogProductOption)
    product = models.ForeignKey(CatalogProductEntity)
    image = models.CharField(max_length=255)
    image_width = models.IntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_template = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imageoption'
        unique_together = (('option_type_id', 'option_id', 'product_id'),)


class ImageoptionTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    short_descrip = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField()
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imageoption_template'


class ImageoptionTemplateOption(models.Model):
    template_option_id = models.AutoField(primary_key=True)
    template = models.ForeignKey(ImageoptionTemplate)
    option = models.ForeignKey(CatalogProductOption)
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imageoption_template_option'
        unique_together = (('template_id', 'option_id'),)


class ImageoptionTemplateProduct(models.Model):
    template_product_id = models.AutoField(primary_key=True)
    template = models.ForeignKey(ImageoptionTemplate)
    product = models.ForeignKey(CatalogProductEntity)
    applied = models.IntegerField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imageoption_template_product'
        unique_together = (('template_id', 'product_id'),)


class ImageoptionTemplateProductOptionsmap(models.Model):
    optionmap_id = models.AutoField(primary_key=True)
    template_option_id = models.IntegerField()
    product_option_id = models.IntegerField()
    template_product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imageoption_template_product_optionsmap'
        unique_together = (('template_option_id', 'product_option_id'),)


class ImageoptionTemplateProductOptiontypesmap(models.Model):
    optiontypemap_id = models.AutoField(primary_key=True)
    template_option_type_id = models.IntegerField()
    product_option_type_id = models.IntegerField()
    optionmap = models.ForeignKey(ImageoptionTemplateProductOptionsmap)

    class Meta:
        managed = False
        db_table = 'imageoption_template_product_optiontypesmap'
        unique_together = (('template_option_type_id', 'product_option_type_id'),)


class ImportexportImportdata(models.Model):
    entity = models.CharField(max_length=50)
    behavior = models.CharField(max_length=10)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'importexport_importdata'


class IndexEvent(models.Model):
    event_id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=64)
    entity = models.CharField(max_length=64)
    entity_pk = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    old_data = models.TextField(blank=True, null=True)
    new_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_event'
        unique_together = (('type', 'entity', 'entity_pk'),)


class IndexProcess(models.Model):
    process_id = models.AutoField(primary_key=True)
    indexer_code = models.CharField(unique=True, max_length=32)
    status = models.CharField(max_length=15)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    mode = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'index_process'


class IndexProcessEvent(models.Model):
    process = models.ForeignKey(IndexProcess)
    event = models.ForeignKey(IndexEvent)
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'index_process_event'
        unique_together = (('process_id', 'event_id'),)


class InnobyteStockalertOrderItem(models.Model):
    store_id = models.SmallIntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    current_stock = models.IntegerField()
    is_ordered = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'innobyte_stockalert_order_item'
        unique_together = (('store_id', 'product_id'),)


class IpRobotsItem(models.Model):
    item_id = models.SmallIntegerField(primary_key=True)
    type = models.IntegerField()
    url = models.TextField()
    comment = models.TextField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ip_robots_item'


class Livechat(models.Model):
    livechat_id = models.AutoField(primary_key=True)
    bubbleenable = models.CharField(max_length=100)
    bubbletext = models.CharField(max_length=100)
    bubbletitle = models.CharField(max_length=100)
    code = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    getvisitorinfo = models.CharField(max_length=100)
    greetings = models.TextField()
    hideonoffline = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    salt = models.CharField(max_length=200)
    theme = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    usessl = models.CharField(db_column='useSSL', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'livechat'


class LogCustomer(models.Model):
    log_id = models.AutoField(primary_key=True)
    visitor_id = models.BigIntegerField(blank=True, null=True)
    customer_id = models.IntegerField()
    login_at = models.DateTimeField()
    logout_at = models.DateTimeField(blank=True, null=True)
    store_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'log_customer'


class LogQuote(models.Model):
    quote_id = models.IntegerField(primary_key=True)
    visitor_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_quote'


class LogSummary(models.Model):
    summary_id = models.BigIntegerField(primary_key=True)
    store_id = models.SmallIntegerField()
    type_id = models.SmallIntegerField(blank=True, null=True)
    visitor_count = models.IntegerField()
    customer_count = models.IntegerField()
    add_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_summary'


class LogSummaryType(models.Model):
    type_id = models.SmallIntegerField(primary_key=True)
    type_code = models.CharField(max_length=64, blank=True, null=True)
    period = models.SmallIntegerField()
    period_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'log_summary_type'


class LogUrl(models.Model):
    url_id = models.BigIntegerField()
    visitor_id = models.BigIntegerField(blank=True, null=True)
    visit_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_url'


class LogUrlInfo(models.Model):
    url_id = models.BigIntegerField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_url_info'


class LogVisitor(models.Model):
    visitor_id = models.BigIntegerField(primary_key=True)
    session_id = models.CharField(max_length=64, blank=True, null=True)
    first_visit_at = models.DateTimeField(blank=True, null=True)
    last_visit_at = models.DateTimeField()
    last_url_id = models.BigIntegerField()
    store_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'log_visitor'


class LogVisitorInfo(models.Model):
    visitor_id = models.BigIntegerField(primary_key=True)
    http_referer = models.CharField(max_length=255, blank=True, null=True)
    http_user_agent = models.CharField(max_length=255, blank=True, null=True)
    http_accept_charset = models.CharField(max_length=255, blank=True, null=True)
    http_accept_language = models.CharField(max_length=255, blank=True, null=True)
    server_addr = models.CharField(max_length=16, blank=True, null=True)
    remote_addr = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_visitor_info'


class LogVisitorOnline(models.Model):
    visitor_id = models.BigIntegerField(primary_key=True)
    visitor_type = models.CharField(max_length=1)
    remote_addr = models.CharField(max_length=16, blank=True, null=True)
    first_visit_at = models.DateTimeField(blank=True, null=True)
    last_visit_at = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    last_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_visitor_online'


class MEmailEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    uniq_key = models.TextField()
    code = models.CharField(max_length=255)
    args_serialized = models.TextField(blank=True, null=True)
    processed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    store_ids = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'm_email_event'


class MEmailEventTrigger(models.Model):
    event = models.ForeignKey(MEmailEvent)
    trigger_id = models.IntegerField()
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_email_event_trigger'


class MEmailQueue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)
    trigger_id = models.IntegerField()
    chain_id = models.IntegerField()
    uniq_key = models.TextField()
    uniq_key_md5 = models.CharField(max_length=255)
    scheduled_at = models.DateTimeField()
    sent_at = models.DateTimeField(blank=True, null=True)
    attemtps_number = models.IntegerField()
    sender_email = models.CharField(max_length=255)
    sender_name = models.CharField(max_length=255)
    recipient_email = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    subject = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    args_serialized = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_email_queue'


class MEmailRule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    is_system = models.IntegerField()
    conditions_serialized = models.TextField()
    actions_serialized = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_email_rule'


class MEmailTrigger(models.Model):
    trigger_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    store_ids = models.CharField(max_length=255)
    is_active = models.IntegerField()
    active_from = models.DateTimeField(blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    trigger_type = models.CharField(max_length=255)
    event = models.CharField(max_length=255, blank=True, null=True)
    cancellation_event = models.TextField(blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    run_rule_id = models.IntegerField(blank=True, null=True)
    stop_rule_id = models.IntegerField(blank=True, null=True)
    sender_email = models.CharField(max_length=255, blank=True, null=True)
    sender_name = models.CharField(max_length=255, blank=True, null=True)
    copy_email = models.TextField(blank=True, null=True)
    ga_source = models.CharField(max_length=255, blank=True, null=True)
    ga_medium = models.CharField(max_length=255, blank=True, null=True)
    ga_term = models.CharField(max_length=255, blank=True, null=True)
    ga_content = models.CharField(max_length=255, blank=True, null=True)
    ga_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_trigger_sandbox_active = models.IntegerField()
    trigger_sandbox_email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_email_trigger'


class MEmailTriggerChain(models.Model):
    chain_id = models.AutoField(primary_key=True)
    trigger_id = models.IntegerField()
    delay = models.TextField(blank=True, null=True)
    template_id = models.CharField(max_length=255)
    run_rule_id = models.IntegerField(blank=True, null=True)
    stop_rule_id = models.IntegerField(blank=True, null=True)
    coupon_enabled = models.IntegerField()
    coupon_sales_rule_id = models.IntegerField(blank=True, null=True)
    coupon_expires_days = models.IntegerField(blank=True, null=True)
    cross_sells_enabled = models.IntegerField()
    cross_sells_type_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_email_trigger_chain'


class MEmailUnsubscription(models.Model):
    unsubscription_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    trigger_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_email_unsubscription'


class MEmaildesignDesign(models.Model):
    design_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    template_type = models.CharField(max_length=255)
    styles = models.TextField(blank=True, null=True)
    template = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_emaildesign_design'


class MEmaildesignTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    design_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255)
    areas_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_emaildesign_template'


class MEmailreportAggregated(models.Model):
    trigger_id = models.IntegerField()
    period = models.DateField()
    emails = models.IntegerField(blank=True, null=True)
    opens = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    orders = models.IntegerField(blank=True, null=True)
    revenue = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_emailreport_aggregated'
        unique_together = (('trigger_id', 'period'),)


class MEmailreportClick(models.Model):
    queue_id = models.IntegerField()
    trigger_id = models.IntegerField()
    session_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_emailreport_click'
        unique_together = (('queue_id', 'trigger_id', 'session_id'),)


class MEmailreportOpen(models.Model):
    queue_id = models.IntegerField()
    trigger_id = models.IntegerField()
    session_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_emailreport_open'
        unique_together = (('queue_id', 'trigger_id', 'session_id'),)


class MEmailreportOrder(models.Model):
    queue_id = models.IntegerField()
    trigger_id = models.IntegerField()
    session_id = models.CharField(max_length=255)
    revenue = models.DecimalField(max_digits=12, decimal_places=4)
    coupon = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_emailreport_order'
        unique_together = (('queue_id', 'trigger_id', 'session_id'),)


class MEmailreportReview(models.Model):
    queue_id = models.IntegerField()
    trigger_id = models.IntegerField()
    session_id = models.CharField(max_length=255)
    review_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_emailreport_review'
        unique_together = (('queue_id', 'trigger_id', 'session_id'),)


class MEmailsmtpMail(models.Model):
    mail_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    is_plain = models.IntegerField()
    body = models.TextField()
    message = models.TextField(blank=True, null=True)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_emailsmtp_mail'


class MMisspell(models.Model):
    misspell_id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=255)
    trigram = models.CharField(max_length=255)
    freq = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'm_misspell'


class MMisspellSuggest(models.Model):
    suggest_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=255)
    suggest = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'm_misspell_suggest'


class MMstcoreAttachment(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=255)
    entity_type = models.CharField(max_length=255)
    entity_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    size = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_mstcore_attachment'


class MMstcoreLogger(models.Model):
    log_id = models.AutoField(primary_key=True)
    level = models.IntegerField()
    message = models.CharField(max_length=255)
    content = models.TextField()
    trace = models.TextField()
    module = models.CharField(max_length=255)
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_mstcore_logger'


class MMstcoreUrlrewrite(models.Model):
    urlrewrite_id = models.AutoField(primary_key=True)
    url_key = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    entity_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_mstcore_urlrewrite'
        unique_together = (('module', 'type', 'entity_id'), ('url_key', 'module'),)


class MRewardsEarningRule(models.Model):
    earning_rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    active_from = models.DateTimeField(blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255)
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)
    earning_style = models.CharField(max_length=255)
    earn_points = models.IntegerField(blank=True, null=True)
    monetary_step = models.FloatField(blank=True, null=True)
    qty_step = models.IntegerField(blank=True, null=True)
    points_limit = models.IntegerField(blank=True, null=True)
    behavior_trigger = models.CharField(max_length=255)
    sort_order = models.IntegerField(blank=True, null=True)
    is_stop_processing = models.IntegerField()
    param1 = models.CharField(max_length=255)
    history_message = models.TextField(blank=True, null=True)
    email_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_rewards_earning_rule'


class MRewardsEarningRuleCustomerGroup(models.Model):
    earning_rule_customer_group_id = models.AutoField(primary_key=True)
    customer_group = models.ForeignKey(CustomerGroup)
    earning_rule = models.ForeignKey(MRewardsEarningRule)

    class Meta:
        managed = False
        db_table = 'm_rewards_earning_rule_customer_group'


class MRewardsEarningRuleProduct(models.Model):
    earning_rule_product_id = models.AutoField(primary_key=True)
    earning_rule = models.ForeignKey(MRewardsEarningRule)
    er_product = models.ForeignKey(CatalogProductEntity)
    er_website = models.ForeignKey(CoreWebsite)
    er_customer_group = models.ForeignKey(CustomerGroup)

    class Meta:
        managed = False
        db_table = 'm_rewards_earning_rule_product'


class MRewardsEarningRuleWebsite(models.Model):
    earning_rule_website_id = models.AutoField(primary_key=True)
    website = models.ForeignKey(CoreWebsite)
    earning_rule = models.ForeignKey(MRewardsEarningRule)

    class Meta:
        managed = False
        db_table = 'm_rewards_earning_rule_website'


class MRewardsNotificationRule(models.Model):
    notification_rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.IntegerField(blank=True, null=True)
    active_from = models.DateTimeField(blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    is_stop_processing = models.IntegerField()
    type = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_rewards_notification_rule'


class MRewardsNotificationRuleCustomerGroup(models.Model):
    notification_rule_customer_group_id = models.AutoField(primary_key=True)
    customer_group = models.ForeignKey(CustomerGroup)
    notification_rule = models.ForeignKey(MRewardsNotificationRule)

    class Meta:
        managed = False
        db_table = 'm_rewards_notification_rule_customer_group'


class MRewardsNotificationRuleWebsite(models.Model):
    notification_rule_website_id = models.AutoField(primary_key=True)
    website = models.ForeignKey(CoreWebsite)
    notification_rule = models.ForeignKey(MRewardsNotificationRule)

    class Meta:
        managed = False
        db_table = 'm_rewards_notification_rule_website'


class MRewardsPurchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    quote_id = models.IntegerField(unique=True, blank=True, null=True)
    order_id = models.IntegerField(unique=True, blank=True, null=True)
    spend_points = models.IntegerField(blank=True, null=True)
    spend_amount = models.FloatField(blank=True, null=True)
    spend_min_points = models.IntegerField(blank=True, null=True)
    spend_max_points = models.IntegerField(blank=True, null=True)
    earn_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_rewards_purchase'


class MRewardsRate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    rate_from = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_to = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    direction = models.CharField(max_length=255)
    website = models.ForeignKey(CoreWebsite)

    class Meta:
        managed = False
        db_table = 'm_rewards_rate'


class MRewardsRateCustomerGroup(models.Model):
    rate_customer_group_id = models.AutoField(primary_key=True)
    rate = models.ForeignKey(MRewardsRate)
    customer_group = models.ForeignKey(CustomerGroup)

    class Meta:
        managed = False
        db_table = 'm_rewards_rate_customer_group'


class MRewardsReferral(models.Model):
    referral_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity)
    new_customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    store = models.ForeignKey(CoreStore)
    last_transaction = models.ForeignKey('MRewardsTransaction', blank=True, null=True)
    points_amount = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    quote_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_rewards_referral'


class MRewardsSpendingRule(models.Model):
    spending_rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    active_from = models.DateTimeField(blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255)
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)
    spending_style = models.CharField(max_length=255)
    spend_points = models.IntegerField(blank=True, null=True)
    monetary_step = models.FloatField(blank=True, null=True)
    spend_min_points = models.CharField(max_length=255)
    spend_max_points = models.CharField(max_length=255)
    sort_order = models.IntegerField(blank=True, null=True)
    is_stop_processing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_rewards_spending_rule'


class MRewardsSpendingRuleCustomerGroup(models.Model):
    spending_rule_customer_group_id = models.AutoField(primary_key=True)
    customer_group = models.ForeignKey(CustomerGroup)
    spending_rule = models.ForeignKey(MRewardsSpendingRule)

    class Meta:
        managed = False
        db_table = 'm_rewards_spending_rule_customer_group'


class MRewardsSpendingRuleWebsite(models.Model):
    spending_rule_website_id = models.AutoField(primary_key=True)
    website = models.ForeignKey(CoreWebsite)
    spending_rule = models.ForeignKey(MRewardsSpendingRule)

    class Meta:
        managed = False
        db_table = 'm_rewards_spending_rule_website'


class MRewardsTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity)
    amount = models.IntegerField(blank=True, null=True)
    amount_used = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=255)
    is_expired = models.IntegerField()
    is_expiration_email_sent = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_rewards_transaction'


class MSearchindex(models.Model):
    index_id = models.AutoField(primary_key=True)
    index_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    position = models.IntegerField()
    attributes_serialized = models.TextField(blank=True, null=True)
    properties_serialized = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    is_active = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex'


class MSearchindexAwBlogPost32(models.Model):
    post_id = models.IntegerField()
    store_id = models.IntegerField()
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    data_index = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    short_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex_aw_blog_post_32'
        unique_together = (('post_id', 'store_id'),)


class MSearchindexAzebizSupportKbarticle(models.Model):
    kb_article_id = models.IntegerField()
    store_id = models.IntegerField()
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    data_index = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    kb_article_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex_azebiz_support_kbarticle'
        unique_together = (('kb_article_id', 'store_id'),)


class MSearchindexExternalWordpressPost(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    store_id = models.IntegerField()
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    data_index = models.TextField(blank=True, null=True)
    post_title = models.TextField(blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    post_excerpt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex_external_wordpress_post'
        unique_together = (('ID', 'store_id'),)


class MSearchindexExternalWordpressPost4(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    store_id = models.IntegerField()
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    data_index = models.TextField(blank=True, null=True)
    post_title = models.TextField(blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    post_excerpt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex_external_wordpress_post_4'
        unique_together = (('ID', 'store_id'),)


class MSearchindexMageCmsPage(models.Model):
    page_id = models.IntegerField()
    store_id = models.IntegerField()
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    data_index = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex_mage_cms_page'
        unique_together = (('page_id', 'store_id'),)


class MSearchindexMageCmsPage2(models.Model):
    page_id = models.IntegerField()
    store_id = models.IntegerField()
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    data_index = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex_mage_cms_page_2'
        unique_together = (('page_id', 'store_id'),)


class MSearchindexTmKnowledgebaseFaq(models.Model):
    id = models.IntegerField()
    store_id = models.IntegerField()
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    data_index = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex_tm_knowledgebase_faq'
        unique_together = (('id', 'store_id'),)


class MSearchindexTmKnowledgebaseFaq31(models.Model):
    id = models.IntegerField()
    store_id = models.IntegerField()
    updated = models.IntegerField()
    searchindex_weight = models.IntegerField()
    data_index = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_searchindex_tm_knowledgebase_faq_31'
        unique_together = (('id', 'store_id'),)


class MSearchlandingpage(models.Model):
    page_id = models.AutoField(primary_key=True)
    query_text = models.CharField(max_length=255)
    url_key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255)
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    layout = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_searchlandingpage'


class MSearchlandingpageStore(models.Model):
    page_store_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(MSearchlandingpage)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'm_searchlandingpage_store'


class MSearchsphinxStopword(models.Model):
    stopword_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255)
    store = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_searchsphinx_stopword'


class MSearchsphinxSynonym(models.Model):
    synonym_id = models.AutoField(primary_key=True)
    synonyms = models.TextField()
    store = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_searchsphinx_synonym'


class MSeoRedirect(models.Model):
    redirect_id = models.AutoField(primary_key=True)
    url_from = models.TextField()
    url_to = models.TextField()
    is_redirect_only_error_page = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    redirect_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_seo_redirect'


class MSeoRedirectStore(models.Model):
    redirect = models.ForeignKey(MSeoRedirect)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'm_seo_redirect_store'


class MSeoRewrite(models.Model):
    rewrite_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_seo_rewrite'


class MSeoRewriteStore(models.Model):
    rewrite = models.ForeignKey(MSeoRewrite)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'm_seo_rewrite_store'


class MSeoTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    rule_type = models.IntegerField()
    sort_order = models.IntegerField()
    conditions_serialized = models.TextField()
    actions_serialized = models.TextField()
    stop_rules_processing = models.IntegerField()
    apply_for_child_categories = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_seo_template'


class MSeoTemplateStore(models.Model):
    template = models.ForeignKey(MSeoTemplate)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'm_seo_template_store'


class MSeoautolinkLink(models.Model):
    link_id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=255)
    url = models.TextField()
    url_target = models.CharField(max_length=255, blank=True, null=True)
    url_title = models.CharField(max_length=255, blank=True, null=True)
    is_nofollow = models.IntegerField()
    max_replacements = models.IntegerField()
    sort_order = models.IntegerField()
    occurence = models.IntegerField()
    is_active = models.IntegerField()
    active_from = models.DateTimeField(blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'm_seoautolink_link'


class MSeoautolinkLinkToStore(models.Model):
    link = models.ForeignKey(MSeoautolinkLink)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'm_seoautolink_link_to_store'


class MSeofilterRewrite(models.Model):
    rewrite_id = models.AutoField(primary_key=True)
    attribute_code = models.CharField(max_length=60)
    option = models.ForeignKey(EavAttributeOption)
    rewrite = models.CharField(max_length=60)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'm_seofilter_rewrite'
        unique_together = (('attribute_code', 'option_id', 'store_id'), ('rewrite', 'store_id'),)


class MagemonkeyApiDebug(models.Model):
    debug_id = models.AutoField(primary_key=True)
    debug_at = models.DateTimeField()
    request_body = models.TextField(blank=True, null=True)
    response_body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magemonkey_api_debug'


class MagemonkeyAsyncOrders(models.Model):
    info = models.TextField()
    created_at = models.DateTimeField()
    processed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magemonkey_async_orders'


class MagemonkeyAsyncSubscribers(models.Model):
    email = models.CharField(max_length=128, blank=True, null=True)
    confirm = models.SmallIntegerField(blank=True, null=True)
    lists = models.TextField()
    mapfields = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    processed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magemonkey_async_subscribers'


class MagemonkeyBulksyncExport(models.Model):
    lists = models.TextField()
    processed_count = models.IntegerField()
    last_processed_id = models.IntegerField()
    status = models.CharField(max_length=13)
    data_source_entity = models.CharField(max_length=21)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    total_count = models.IntegerField()
    started_at = models.DateTimeField(blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magemonkey_bulksync_export'


class MagemonkeyBulksyncImport(models.Model):
    lists = models.TextField()
    import_types = models.TextField()
    status = models.CharField(max_length=13)
    create_customer = models.IntegerField()
    last_processed_id = models.IntegerField()
    processed_count = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    since = models.DateTimeField(blank=True, null=True)
    total_count = models.IntegerField()
    started_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magemonkey_bulksync_import'


class MagemonkeyEcommerce360(models.Model):
    order_id = models.IntegerField()
    order_increment_id = models.CharField(max_length=50)
    mc_campaign_id = models.CharField(max_length=255)
    mc_email_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    store_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magemonkey_ecommerce360'


class MagemonkeyLastOrder(models.Model):
    email = models.CharField(max_length=128, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'magemonkey_last_order'


class MagemonkeyMailsSent(models.Model):
    store_id = models.SmallIntegerField(blank=True, null=True)
    mail_type = models.CharField(max_length=16)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    coupon_number = models.CharField(max_length=255, blank=True, null=True)
    coupon_type = models.SmallIntegerField(blank=True, null=True)
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sent_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'magemonkey_mails_sent'


class Magenotification(models.Model):
    magenotification_id = models.AutoField(primary_key=True)
    notification_id = models.IntegerField()
    url = models.CharField(max_length=255)
    added_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'magenotification'
        unique_together = (('notification_id', 'url'),)


class MagenotificationExtensionFeedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    extension_version = models.CharField(max_length=50)
    coupon_code = models.CharField(max_length=255)
    coupon_value = models.CharField(max_length=50)
    expired_counpon = models.DateTimeField()
    content = models.TextField()
    file = models.TextField()
    comment = models.TextField()
    latest_message = models.TextField()
    latest_response = models.TextField()
    latest_response_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    is_sent = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'magenotification_extension_feedback'


class MagenotificationExtensionFeedbackmessage(models.Model):
    feedbackmessage_id = models.AutoField(primary_key=True)
    feedback_id = models.IntegerField()
    feedback_code = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    is_customer = models.IntegerField(blank=True, null=True)
    message = models.TextField()
    file = models.TextField()
    posted_time = models.DateTimeField(blank=True, null=True)
    is_sent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magenotification_extension_feedbackmessage'


class MagenotificationLicense(models.Model):
    license_id = models.AutoField(primary_key=True)
    extension_code = models.CharField(max_length=100)
    license_key = models.TextField()
    active_at = models.DateField()
    sum_code = models.CharField(max_length=255, blank=True, null=True)
    response_code = models.SmallIntegerField(blank=True, null=True)
    domains = models.CharField(max_length=255, blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magenotification_license'


class MagenotificationLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    extension_code = models.CharField(max_length=100)
    license_type = models.CharField(max_length=50)
    license_key = models.TextField()
    check_date = models.DateField()
    sum_code = models.CharField(max_length=255, blank=True, null=True)
    response_code = models.SmallIntegerField(blank=True, null=True)
    expired_time = models.CharField(max_length=255, blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magenotification_log'


class MageworxCustomOptionsGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    is_active = models.IntegerField()
    hash_options = models.TextField()
    absolute_price = models.IntegerField()
    absolute_weight = models.IntegerField()
    sku_policy = models.IntegerField()
    update_inventory = models.IntegerField()
    only_update = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_group'


class MageworxCustomOptionsGroupStore(models.Model):
    group_store_id = models.AutoField(primary_key=True)
    group = models.ForeignKey(MageworxCustomOptionsGroup)
    store_id = models.SmallIntegerField()
    hash_options = models.TextField()

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_group_store'
        unique_together = (('group_id', 'store_id'),)


class MageworxCustomOptionsOptionDefault(models.Model):
    option_default_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption)
    store = models.ForeignKey(CoreStore)
    default_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_option_default'
        unique_together = (('option_id', 'store_id'),)


class MageworxCustomOptionsOptionDescription(models.Model):
    option_description_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption)
    store = models.ForeignKey(CoreStore)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_option_description'


class MageworxCustomOptionsOptionTypeDescription(models.Model):
    option_type_description_id = models.AutoField(primary_key=True)
    option_type = models.ForeignKey(CatalogProductOptionTypeValue)
    store = models.ForeignKey(CoreStore)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_option_type_description'
        unique_together = (('option_type_id', 'store_id'),)


class MageworxCustomOptionsOptionTypeImage(models.Model):
    option_type_image_id = models.AutoField(primary_key=True)
    option_type = models.ForeignKey(CatalogProductOptionTypeValue)
    image_file = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()
    source = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_option_type_image'


class MageworxCustomOptionsOptionTypeSpecialPrice(models.Model):
    option_type_special_price_id = models.AutoField(primary_key=True)
    option_type_price = models.ForeignKey(CatalogProductOptionTypePrice)
    customer_group_id = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4)
    price_type = models.CharField(max_length=7)
    comment = models.CharField(max_length=255)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_option_type_special_price'
        unique_together = (('option_type_price_id', 'customer_group_id'),)


class MageworxCustomOptionsOptionTypeTierPrice(models.Model):
    option_type_tier_price_id = models.AutoField(primary_key=True)
    option_type_price = models.ForeignKey(CatalogProductOptionTypePrice)
    customer_group_id = models.SmallIntegerField()
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4)
    price_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_option_type_tier_price'
        unique_together = (('option_type_price_id', 'customer_group_id', 'qty'),)


class MageworxCustomOptionsOptionViewMode(models.Model):
    view_mode_id = models.AutoField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption)
    store = models.ForeignKey(CoreStore)
    view_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_option_view_mode'
        unique_together = (('option_id', 'store_id'),)


class MageworxCustomOptionsRelation(models.Model):
    group = models.ForeignKey(MageworxCustomOptionsGroup)
    product = models.ForeignKey(CatalogProductEntity)
    option_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_custom_options_relation'
        unique_together = (('group_id', 'option_id', 'product_id'),)


class MageworxDeliveryzoneCategories(models.Model):
    entity_id = models.AutoField(primary_key=True)
    zone_id = models.SmallIntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_categories'


class MageworxDeliveryzoneCustomerGroupCarriers(models.Model):
    entity_id = models.AutoField(primary_key=True)
    customer_group_id = models.SmallIntegerField()
    carrier_id = models.CharField(max_length=255)
    allowed_methods = models.TextField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_customer_group_carriers'


class MageworxDeliveryzoneLocations(models.Model):
    entity_id = models.AutoField(primary_key=True)
    zone_id = models.SmallIntegerField()
    country_id = models.CharField(max_length=2)
    region_ids = models.TextField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_locations'


class MageworxDeliveryzoneProducts(models.Model):
    entity_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    zone_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_products'


class MageworxDeliveryzoneRates(models.Model):
    rate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)
    simple_action = models.CharField(max_length=20)
    shipping_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    surcharge_fixed = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    surcharge_percent = models.FloatField()
    fixed_per_product = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    percent_per_product = models.FloatField()
    percent_per_item = models.FloatField()
    fixed_per_item = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    percent_per_order = models.FloatField()
    fixed_per_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    sort_order = models.IntegerField()
    stop_processing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_rates'


class MageworxDeliveryzoneRatesCarrier(models.Model):
    entity_id = models.AutoField(primary_key=True)
    rate_id = models.IntegerField()
    carrier = models.CharField(max_length=50)
    method_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_rates_carrier'


class MageworxDeliveryzoneRatesCustomergroup(models.Model):
    entity_id = models.AutoField(primary_key=True)
    rate_id = models.IntegerField()
    customergroup_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_rates_customergroup'


class MageworxDeliveryzoneRatesStore(models.Model):
    entity_id = models.AutoField(primary_key=True)
    rate_id = models.IntegerField()
    store_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_rates_store'


class MageworxDeliveryzoneShippingmethods(models.Model):
    entity_id = models.AutoField(primary_key=True)
    carrier_id = models.CharField(max_length=255)
    zone_id = models.SmallIntegerField()
    allowed_methods = models.TextField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_shippingmethods'


class MageworxDeliveryzoneZones(models.Model):
    zone_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mageworx_deliveryzone_zones'


class MageworxOrderseditOrderStatusHistory(models.Model):
    entity_id = models.AutoField(primary_key=True)
    history = models.ForeignKey('SalesFlatOrderStatusHistory', unique=True)
    creator_admin_user_id = models.IntegerField()
    creator_firstname = models.CharField(max_length=32)
    creator_lastname = models.CharField(max_length=32)
    creator_username = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mageworx_ordersedit_order_status_history'


class MageworxOrdersgridOrderGroup(models.Model):
    order_group_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mageworx_ordersgrid_order_group'


class MwMcoreNotification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=25)
    message = models.TextField()
    time_apply = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()
    message_id = models.IntegerField(blank=True, null=True)
    extension_key = models.CharField(max_length=25, blank=True, null=True)
    current_display = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mw_mcore_notification'


class MwOnestepcheckout(models.Model):
    mw_onestepcheckout_date_id = models.AutoField(primary_key=True)
    sales_order_id = models.IntegerField()
    mw_customercomment_info = models.CharField(max_length=255, blank=True, null=True)
    mw_deliverydate_date = models.CharField(max_length=15, blank=True, null=True)
    mw_deliverydate_time = models.CharField(max_length=55, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mw_onestepcheckout'


class NewsletterProblem(models.Model):
    problem_id = models.AutoField(primary_key=True)
    subscriber = models.ForeignKey('NewsletterSubscriber', blank=True, null=True)
    queue = models.ForeignKey('NewsletterQueue')
    problem_error_code = models.IntegerField(blank=True, null=True)
    problem_error_text = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_problem'


class NewsletterQueue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    template = models.ForeignKey('NewsletterTemplate')
    newsletter_type = models.IntegerField(blank=True, null=True)
    newsletter_text = models.TextField(blank=True, null=True)
    newsletter_styles = models.TextField(blank=True, null=True)
    newsletter_subject = models.CharField(max_length=200, blank=True, null=True)
    newsletter_sender_name = models.CharField(max_length=200, blank=True, null=True)
    newsletter_sender_email = models.CharField(max_length=200, blank=True, null=True)
    queue_status = models.IntegerField()
    queue_start_at = models.DateTimeField(blank=True, null=True)
    queue_finish_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_queue'


class NewsletterQueueLink(models.Model):
    queue_link_id = models.AutoField(primary_key=True)
    queue = models.ForeignKey(NewsletterQueue)
    subscriber = models.ForeignKey('NewsletterSubscriber')
    letter_sent_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_queue_link'


class NewsletterQueueStoreLink(models.Model):
    queue = models.ForeignKey(NewsletterQueue)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'newsletter_queue_store_link'
        unique_together = (('queue_id', 'store_id'),)


class NewsletterSubscriber(models.Model):
    subscriber_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    change_status_at = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField()
    subscriber_email = models.CharField(max_length=150, blank=True, null=True)
    subscriber_status = models.IntegerField()
    subscriber_confirm_code = models.CharField(max_length=32, blank=True, null=True)
    subscriber_firstname = models.CharField(max_length=50, blank=True, null=True)
    subscriber_lastname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_subscriber'


class NewsletterTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    template_code = models.CharField(max_length=150, blank=True, null=True)
    template_text = models.TextField(blank=True, null=True)
    template_text_preprocessed = models.TextField(blank=True, null=True)
    template_styles = models.TextField(blank=True, null=True)
    template_type = models.IntegerField(blank=True, null=True)
    template_subject = models.CharField(max_length=200, blank=True, null=True)
    template_sender_name = models.CharField(max_length=200, blank=True, null=True)
    template_sender_email = models.CharField(max_length=200, blank=True, null=True)
    template_actual = models.SmallIntegerField(blank=True, null=True)
    added_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_template'


class OauthConsumer(models.Model):
    entity_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    key = models.CharField(unique=True, max_length=32)
    secret = models.CharField(unique=True, max_length=32)
    callback_url = models.CharField(max_length=255, blank=True, null=True)
    rejected_callback_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oauth_consumer'


class OauthNonce(models.Model):
    nonce = models.CharField(unique=True, max_length=32)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oauth_nonce'


class OauthToken(models.Model):
    entity_id = models.AutoField(primary_key=True)
    consumer = models.ForeignKey(OauthConsumer)
    admin = models.ForeignKey(AdminUser, blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    type = models.CharField(max_length=16)
    token = models.CharField(unique=True, max_length=32)
    secret = models.CharField(max_length=32)
    verifier = models.CharField(max_length=32, blank=True, null=True)
    callback_url = models.CharField(max_length=255)
    revoked = models.SmallIntegerField()
    authorized = models.SmallIntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oauth_token'


class OrdersexporttoolAttributes(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_name = models.CharField(max_length=100)
    attribute_order_item = models.TextField(blank=True, null=True)
    attribute_order_address = models.TextField(blank=True, null=True)
    attribute_order_payment = models.TextField(blank=True, null=True)
    attribute_invoice = models.TextField(blank=True, null=True)
    attribute_shipment = models.TextField(blank=True, null=True)
    attribute_creditmemo = models.TextField(blank=True, null=True)
    attribute_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordersexporttool_attributes'


class OrdersexporttoolProfiles(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=90)
    file_type = models.IntegerField()
    file_path = models.CharField(max_length=255)
    file_store_id = models.CharField(max_length=255)
    file_flag = models.IntegerField()
    file_single_export = models.IntegerField()
    file_updated_at = models.DateTimeField()
    file_last_exported_id = models.IntegerField(blank=True, null=True)
    file_first_exported_id = models.IntegerField(blank=True, null=True)
    file_automatically_update_last_order_id = models.IntegerField()
    file_date_format = models.CharField(max_length=50)
    file_include_header = models.IntegerField()
    file_repeat_for_each = models.IntegerField()
    file_repeat_for_each_increment = models.IntegerField(blank=True, null=True)
    file_order_by = models.IntegerField()
    file_order_by_field = models.IntegerField(blank=True, null=True)
    file_header = models.TextField(blank=True, null=True)
    file_body = models.TextField(blank=True, null=True)
    file_footer = models.TextField(blank=True, null=True)
    file_separator = models.CharField(max_length=3, blank=True, null=True)
    file_protector = models.CharField(max_length=1, blank=True, null=True)
    file_enclose_data = models.IntegerField()
    file_attributes = models.TextField(blank=True, null=True)
    file_states = models.TextField(blank=True, null=True)
    file_customer_groups = models.TextField(blank=True, null=True)
    file_scheduled_task = models.CharField(max_length=900)
    file_ftp_enabled = models.IntegerField(blank=True, null=True)
    file_ftp_host = models.CharField(max_length=300, blank=True, null=True)
    file_ftp_login = models.CharField(max_length=300, blank=True, null=True)
    file_ftp_password = models.CharField(max_length=300, blank=True, null=True)
    file_ftp_active = models.IntegerField(blank=True, null=True)
    file_ftp_dir = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordersexporttool_profiles'


class Osconnectkeys(models.Model):
    key_id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=250)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'osconnectkeys'


class PaypalCert(models.Model):
    cert_id = models.SmallIntegerField(primary_key=True)
    website = models.ForeignKey(CoreWebsite)
    content = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_cert'


class PaypalPaymentTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    txn_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_payment_transaction'


class PaypalSettlementReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_date = models.DateTimeField(blank=True, null=True)
    account_id = models.CharField(max_length=64, blank=True, null=True)
    filename = models.CharField(max_length=24, blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_settlement_report'
        unique_together = (('report_date', 'account_id'),)


class PaypalSettlementReportRow(models.Model):
    row_id = models.AutoField(primary_key=True)
    report = models.ForeignKey(PaypalSettlementReport)
    transaction_id = models.CharField(max_length=19, blank=True, null=True)
    invoice_id = models.CharField(max_length=127, blank=True, null=True)
    paypal_reference_id = models.CharField(max_length=19, blank=True, null=True)
    paypal_reference_id_type = models.CharField(max_length=3, blank=True, null=True)
    transaction_event_code = models.CharField(max_length=5, blank=True, null=True)
    transaction_initiation_date = models.DateTimeField(blank=True, null=True)
    transaction_completion_date = models.DateTimeField(blank=True, null=True)
    transaction_debit_or_credit = models.CharField(max_length=2)
    gross_transaction_amount = models.DecimalField(max_digits=20, decimal_places=6)
    gross_transaction_currency = models.CharField(max_length=3, blank=True, null=True)
    fee_debit_or_credit = models.CharField(max_length=2, blank=True, null=True)
    fee_amount = models.DecimalField(max_digits=20, decimal_places=6)
    fee_currency = models.CharField(max_length=3, blank=True, null=True)
    custom_field = models.CharField(max_length=255, blank=True, null=True)
    consumer_id = models.CharField(max_length=127, blank=True, null=True)
    payment_tracking_id = models.CharField(max_length=255, blank=True, null=True)
    store_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_settlement_report_row'


class PaypalauthCustomer(models.Model):
    payer_id = models.CharField(unique=True, max_length=255)
    customer = models.ForeignKey(CustomerEntity, unique=True)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'paypalauth_customer'


class PermissionBlock(models.Model):
    block_id = models.AutoField(primary_key=True)
    block_name = models.CharField(unique=True, max_length=255)
    is_allowed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permission_block'


class PermissionVariable(models.Model):
    variable_id = models.AutoField()
    variable_name = models.CharField(unique=True, max_length=255)
    is_allowed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permission_variable'
        unique_together = (('variable_id', 'variable_name'),)


class PersistentSession(models.Model):
    persistent_id = models.AutoField(primary_key=True)
    key = models.CharField(unique=True, max_length=50)
    customer = models.ForeignKey(CustomerEntity, unique=True, blank=True, null=True)
    website = models.ForeignKey(CoreWebsite)
    info = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persistent_session'


class Poll(models.Model):
    poll_id = models.AutoField(primary_key=True)
    poll_title = models.CharField(max_length=255, blank=True, null=True)
    votes_count = models.IntegerField()
    store = models.ForeignKey(CoreStore)
    date_posted = models.DateTimeField()
    date_closed = models.DateTimeField(blank=True, null=True)
    active = models.SmallIntegerField()
    closed = models.SmallIntegerField()
    answers_display = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poll'


class PollAnswer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Poll)
    answer_title = models.CharField(max_length=255, blank=True, null=True)
    votes_count = models.IntegerField()
    answer_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'poll_answer'


class PollStore(models.Model):
    poll = models.ForeignKey(Poll)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'poll_store'
        unique_together = (('poll_id', 'store_id'),)


class PollVote(models.Model):
    vote_id = models.AutoField(primary_key=True)
    poll_id = models.IntegerField()
    poll_answer = models.ForeignKey(PollAnswer)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    vote_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poll_vote'


class ProductAlertPrice(models.Model):
    alert_price_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity)
    product = models.ForeignKey(CatalogProductEntity)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    website = models.ForeignKey(CoreWebsite)
    add_date = models.DateTimeField()
    last_send_date = models.DateTimeField(blank=True, null=True)
    send_count = models.SmallIntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'product_alert_price'


class ProductAlertStock(models.Model):
    alert_stock_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    product = models.ForeignKey(CatalogProductEntity)
    website = models.ForeignKey(CoreWebsite)
    add_date = models.DateTimeField()
    send_date = models.DateTimeField(blank=True, null=True)
    send_count = models.SmallIntegerField()
    status = models.SmallIntegerField()
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_alert_stock'


class Rating(models.Model):
    rating_id = models.SmallIntegerField(primary_key=True)
    entity = models.ForeignKey('RatingEntity')
    rating_code = models.CharField(unique=True, max_length=64)
    position = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rating'


class RatingEntity(models.Model):
    entity_id = models.SmallIntegerField(primary_key=True)
    entity_code = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'rating_entity'


class RatingOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    rating = models.ForeignKey(Rating)
    code = models.CharField(max_length=32)
    value = models.SmallIntegerField()
    position = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rating_option'


class RatingOptionVote(models.Model):
    vote_id = models.BigIntegerField(primary_key=True)
    option = models.ForeignKey(RatingOption)
    remote_ip = models.CharField(max_length=50, blank=True, null=True)
    remote_ip_long = models.CharField(max_length=16, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    entity_pk_value = models.BigIntegerField()
    rating_id = models.SmallIntegerField()
    review = models.ForeignKey('Review', blank=True, null=True)
    percent = models.SmallIntegerField()
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rating_option_vote'


class RatingOptionVoteAggregated(models.Model):
    primary_id = models.AutoField(primary_key=True)
    rating = models.ForeignKey(Rating)
    entity_pk_value = models.BigIntegerField()
    vote_count = models.IntegerField()
    vote_value_sum = models.IntegerField()
    percent = models.SmallIntegerField()
    percent_approved = models.SmallIntegerField(blank=True, null=True)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'rating_option_vote_aggregated'


class RatingStore(models.Model):
    rating = models.ForeignKey(Rating)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'rating_store'
        unique_together = (('rating_id', 'store_id'),)


class RatingTitle(models.Model):
    rating = models.ForeignKey(Rating)
    store = models.ForeignKey(CoreStore)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rating_title'
        unique_together = (('rating_id', 'store_id'),)


class ReportComparedProductIndex(models.Model):
    index_id = models.BigIntegerField(primary_key=True)
    visitor_id = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    added_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'report_compared_product_index'
        unique_together = (('visitor_id', 'product_id'), ('customer_id', 'product_id'),)


class ReportEvent(models.Model):
    event_id = models.BigIntegerField(primary_key=True)
    logged_at = models.DateTimeField()
    event_type = models.ForeignKey('ReportEventTypes')
    object_id = models.IntegerField()
    subject_id = models.IntegerField()
    subtype = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'report_event'


class ReportEventTypes(models.Model):
    event_type_id = models.SmallIntegerField(primary_key=True)
    event_name = models.CharField(max_length=64)
    customer_login = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'report_event_types'


class ReportViewedProductAggregatedDaily(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    views_num = models.IntegerField()
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'report_viewed_product_aggregated_daily'
        unique_together = (('period', 'store_id', 'product_id'),)


class ReportViewedProductAggregatedMonthly(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    views_num = models.IntegerField()
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'report_viewed_product_aggregated_monthly'
        unique_together = (('period', 'store_id', 'product_id'),)


class ReportViewedProductAggregatedYearly(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    views_num = models.IntegerField()
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'report_viewed_product_aggregated_yearly'
        unique_together = (('period', 'store_id', 'product_id'),)


class ReportViewedProductIndex(models.Model):
    index_id = models.BigIntegerField(primary_key=True)
    visitor_id = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    added_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'report_viewed_product_index'
        unique_together = (('customer_id', 'product_id'), ('visitor_id', 'product_id'),)


class Review(models.Model):
    review_id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    entity = models.ForeignKey('ReviewEntity')
    entity_pk_value = models.IntegerField()
    status = models.ForeignKey('ReviewStatus')

    class Meta:
        managed = False
        db_table = 'review'


class ReviewDetail(models.Model):
    detail_id = models.BigIntegerField(primary_key=True)
    review = models.ForeignKey(Review)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    title = models.CharField(max_length=255)
    detail = models.TextField()
    nickname = models.CharField(max_length=128)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_detail'


class ReviewEntity(models.Model):
    entity_id = models.SmallIntegerField(primary_key=True)
    entity_code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'review_entity'


class ReviewEntitySummary(models.Model):
    primary_id = models.BigIntegerField(primary_key=True)
    entity_pk_value = models.BigIntegerField()
    entity_type = models.SmallIntegerField()
    reviews_count = models.SmallIntegerField()
    rating_summary = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'review_entity_summary'


class ReviewStatus(models.Model):
    status_id = models.SmallIntegerField(primary_key=True)
    status_code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'review_status'


class ReviewStore(models.Model):
    review = models.ForeignKey(Review)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'review_store'
        unique_together = (('review_id', 'store_id'),)


class SalesBestsellersAggregatedDaily(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_bestsellers_aggregated_daily'
        unique_together = (('period', 'store_id', 'product_id'),)


class SalesBestsellersAggregatedMonthly(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_bestsellers_aggregated_monthly'
        unique_together = (('period', 'store_id', 'product_id'),)


class SalesBestsellersAggregatedYearly(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_bestsellers_aggregated_yearly'
        unique_together = (('period', 'store_id', 'product_id'),)


class SalesBillingAgreement(models.Model):
    agreement_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity)
    method_code = models.CharField(max_length=32)
    reference_id = models.CharField(max_length=32)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    agreement_label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_billing_agreement'


class SalesBillingAgreementOrder(models.Model):
    agreement = models.ForeignKey(SalesBillingAgreement)
    order = models.ForeignKey('SalesFlatOrder')

    class Meta:
        managed = False
        db_table = 'sales_billing_agreement_order'
        unique_together = (('agreement_id', 'order_id'),)


class SalesFlatCreditmemo(models.Model):
    entity_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    adjustment = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order = models.ForeignKey('SalesFlatOrder')
    email_sent = models.SmallIntegerField(blank=True, null=True)
    creditmemo_status = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    order_currency_code = models.CharField(max_length=3, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    transaction_key = models.CharField(max_length=50, blank=True, null=True)
    buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    jirafe_export_status = models.IntegerField(blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)
    eboekhouden_mutatie = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_creditmemo'


class SalesFlatCreditmemoComment(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatCreditmemo)
    is_customer_notified = models.IntegerField(blank=True, null=True)
    is_visible_on_front = models.SmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_creditmemo_comment'


class SalesFlatCreditmemoGrid(models.Model):
    entity = models.ForeignKey(SalesFlatCreditmemo, primary_key=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_id = models.IntegerField()
    creditmemo_status = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    order_currency_code = models.CharField(max_length=3, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    order_increment_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    order_created_at = models.DateTimeField(blank=True, null=True)
    billing_name = models.CharField(max_length=255, blank=True, null=True)
    eboekhouden_mutatie = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_creditmemo_grid'


class SalesFlatCreditmemoItem(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatCreditmemo)
    base_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied = models.TextField(blank=True, null=True)
    base_weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_row_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_row_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_creditmemo_item'


class SalesFlatInvoice(models.Model):
    entity_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    is_used_for_refund = models.SmallIntegerField(blank=True, null=True)
    order = models.ForeignKey('SalesFlatOrder')
    email_sent = models.SmallIntegerField(blank=True, null=True)
    can_void_flag = models.SmallIntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    order_currency_code = models.CharField(max_length=3, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)
    eboekhouden_mutatie = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_invoice'


class SalesFlatInvoiceComment(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatInvoice)
    is_customer_notified = models.SmallIntegerField(blank=True, null=True)
    is_visible_on_front = models.SmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_invoice_comment'


class SalesFlatInvoiceGrid(models.Model):
    entity = models.ForeignKey(SalesFlatInvoice, primary_key=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_id = models.IntegerField()
    state = models.IntegerField(blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    order_currency_code = models.CharField(max_length=3, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    order_increment_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    order_created_at = models.DateTimeField(blank=True, null=True)
    billing_name = models.CharField(max_length=255, blank=True, null=True)
    eboekhouden_mutatie = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_invoice_grid'


class SalesFlatInvoiceItem(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatInvoice)
    base_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_row_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_row_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied = models.TextField(blank=True, null=True)
    weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_invoice_item'


class SalesFlatOrder(models.Model):
    entity_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    protect_code = models.CharField(max_length=255, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_invoiced_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    can_ship_partially = models.SmallIntegerField(blank=True, null=True)
    can_ship_partially_item = models.SmallIntegerField(blank=True, null=True)
    customer_is_guest = models.SmallIntegerField(blank=True, null=True)
    customer_note_notify = models.SmallIntegerField(blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    customer_group_id = models.SmallIntegerField(blank=True, null=True)
    edit_increment = models.IntegerField(blank=True, null=True)
    email_sent = models.SmallIntegerField(blank=True, null=True)
    forced_shipment_with_invoice = models.SmallIntegerField(blank=True, null=True)
    payment_auth_expiration = models.IntegerField(blank=True, null=True)
    quote_address_id = models.IntegerField(blank=True, null=True)
    quote_id = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_due = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    payment_authorization_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_due = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    customer_dob = models.DateTimeField(blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    applied_rule_ids = models.CharField(max_length=255, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_firstname = models.CharField(max_length=255, blank=True, null=True)
    customer_lastname = models.CharField(max_length=255, blank=True, null=True)
    customer_middlename = models.CharField(max_length=255, blank=True, null=True)
    customer_prefix = models.CharField(max_length=255, blank=True, null=True)
    customer_suffix = models.CharField(max_length=255, blank=True, null=True)
    customer_taxvat = models.CharField(max_length=255, blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)
    ext_customer_id = models.CharField(max_length=255, blank=True, null=True)
    ext_order_id = models.CharField(max_length=255, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    hold_before_state = models.CharField(max_length=255, blank=True, null=True)
    hold_before_status = models.CharField(max_length=255, blank=True, null=True)
    order_currency_code = models.CharField(max_length=255, blank=True, null=True)
    original_increment_id = models.CharField(max_length=50, blank=True, null=True)
    relation_child_id = models.CharField(max_length=32, blank=True, null=True)
    relation_child_real_id = models.CharField(max_length=32, blank=True, null=True)
    relation_parent_id = models.CharField(max_length=32, blank=True, null=True)
    relation_parent_real_id = models.CharField(max_length=32, blank=True, null=True)
    remote_ip = models.CharField(max_length=255, blank=True, null=True)
    shipping_method = models.CharField(max_length=255, blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    store_name = models.CharField(max_length=255, blank=True, null=True)
    x_forwarded_for = models.CharField(max_length=255, blank=True, null=True)
    customer_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    total_item_count = models.SmallIntegerField()
    customer_gender = models.IntegerField(blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    coupon_rule_name = models.CharField(max_length=255, blank=True, null=True)
    paypal_ipn_customer_notified = models.IntegerField(blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    transaction_key = models.CharField(max_length=50, blank=True, null=True)
    payment_method_used_for_transaction = models.CharField(max_length=50, blank=True, null=True)
    currency_code_used_for_transaction = models.CharField(max_length=3, blank=True, null=True)
    buckaroo_secure_enrolled = models.SmallIntegerField(blank=True, null=True)
    buckaroo_secure_authenticated = models.SmallIntegerField(blank=True, null=True)
    buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    myparcel_consignment_ids = models.TextField(blank=True, null=True)
    buckaroo_service_version_used = models.SmallIntegerField(blank=True, null=True)
    ebizmarts_abandonedcart_flag = models.IntegerField(blank=True, null=True)
    export_flag = models.CharField(max_length=100)
    ebizmarts_magemonkey_campaign_id = models.CharField(max_length=10, blank=True, null=True)
    jirafe_visitor_id = models.CharField(max_length=255, blank=True, null=True)
    jirafe_attribution_data = models.TextField(blank=True, null=True)
    jirafe_export_status = models.IntegerField(blank=True, null=True)
    jirafe_placed_from_frontend = models.IntegerField(blank=True, null=True)
    jirafe_orig_visitor_id = models.CharField(max_length=255, blank=True, null=True)
    is_edited = models.IntegerField()
    order_group_id = models.IntegerField()
    imported = models.IntegerField()
    giftwrap_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_giftwrap_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order'


class SalesFlatOrderAddress(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatOrder, blank=True, null=True)
    customer_address_id = models.IntegerField(blank=True, null=True)
    quote_address_id = models.IntegerField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.CharField(max_length=2, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    address_type = models.CharField(max_length=255, blank=True, null=True)
    prefix = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    vat_id = models.TextField(blank=True, null=True)
    vat_is_valid = models.SmallIntegerField(blank=True, null=True)
    vat_request_id = models.TextField(blank=True, null=True)
    vat_request_date = models.TextField(blank=True, null=True)
    vat_request_success = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_address'


class SalesFlatOrderGrid(models.Model):
    entity = models.ForeignKey(SalesFlatOrder, primary_key=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    store_name = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    order_currency_code = models.CharField(max_length=255, blank=True, null=True)
    shipping_name = models.CharField(max_length=255, blank=True, null=True)
    billing_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    export_flag = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_group_id = models.SmallIntegerField(blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    total_refunded = models.DecimalField(max_digits=12, decimal_places=4)
    shipping_method = models.CharField(max_length=255)
    is_edited = models.IntegerField()
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    base_total_refunded = models.DecimalField(max_digits=12, decimal_places=4)
    shipping_description = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales_flat_order_grid'


class SalesFlatOrderItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(SalesFlatOrder)
    parent_item_id = models.IntegerField(blank=True, null=True)
    quote_item_id = models.IntegerField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    product_id = models.IntegerField(blank=True, null=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    product_options = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    applied_rule_ids = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    free_shipping = models.SmallIntegerField()
    is_qty_decimal = models.SmallIntegerField(blank=True, null=True)
    no_discount = models.SmallIntegerField()
    qty_backordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_shipped = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    base_price = models.DecimalField(max_digits=12, decimal_places=4)
    original_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_original_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4)
    row_invoiced = models.DecimalField(max_digits=12, decimal_places=4)
    base_row_invoiced = models.DecimalField(max_digits=12, decimal_places=4)
    row_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_before_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_before_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    ext_order_item_id = models.CharField(max_length=255, blank=True, null=True)
    locked_do_invoice = models.SmallIntegerField(blank=True, null=True)
    locked_do_ship = models.SmallIntegerField(blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_nominal = models.IntegerField()
    tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    gift_message_available = models.IntegerField(blank=True, null=True)
    base_weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_row_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_row_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied = models.TextField(blank=True, null=True)
    weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_item'


class SalesFlatOrderPayment(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatOrder)
    base_shipping_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_authorized = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_paid_online = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_refunded_online = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_authorized = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    quote_payment_id = models.IntegerField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    cc_exp_month = models.CharField(max_length=255, blank=True, null=True)
    cc_ss_start_year = models.CharField(max_length=255, blank=True, null=True)
    echeck_bank_name = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    cc_debug_request_body = models.CharField(max_length=255, blank=True, null=True)
    cc_secure_verify = models.CharField(max_length=255, blank=True, null=True)
    protection_eligibility = models.CharField(max_length=255, blank=True, null=True)
    cc_approval = models.CharField(max_length=255, blank=True, null=True)
    cc_last4 = models.CharField(max_length=255, blank=True, null=True)
    cc_status_description = models.CharField(max_length=255, blank=True, null=True)
    echeck_type = models.CharField(max_length=255, blank=True, null=True)
    cc_debug_response_serialized = models.CharField(max_length=255, blank=True, null=True)
    cc_ss_start_month = models.CharField(max_length=255, blank=True, null=True)
    echeck_account_type = models.CharField(max_length=255, blank=True, null=True)
    last_trans_id = models.CharField(max_length=255, blank=True, null=True)
    cc_cid_status = models.CharField(max_length=255, blank=True, null=True)
    cc_owner = models.CharField(max_length=255, blank=True, null=True)
    cc_type = models.CharField(max_length=255, blank=True, null=True)
    po_number = models.CharField(max_length=255, blank=True, null=True)
    cc_exp_year = models.CharField(max_length=255, blank=True, null=True)
    cc_status = models.CharField(max_length=255, blank=True, null=True)
    echeck_routing_number = models.CharField(max_length=255, blank=True, null=True)
    account_status = models.CharField(max_length=255, blank=True, null=True)
    anet_trans_method = models.CharField(max_length=255, blank=True, null=True)
    cc_debug_response_body = models.CharField(max_length=255, blank=True, null=True)
    cc_ss_issue = models.CharField(max_length=255, blank=True, null=True)
    echeck_account_name = models.CharField(max_length=255, blank=True, null=True)
    cc_avs_status = models.CharField(max_length=255, blank=True, null=True)
    cc_number_enc = models.CharField(max_length=255, blank=True, null=True)
    cc_trans_id = models.CharField(max_length=255, blank=True, null=True)
    paybox_request_number = models.CharField(max_length=255, blank=True, null=True)
    address_status = models.CharField(max_length=255, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_payment'


class SalesFlatOrderStatusHistory(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatOrder)
    is_customer_notified = models.IntegerField(blank=True, null=True)
    is_visible_on_front = models.SmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    entity_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_status_history'


class SalesFlatQuote(models.Model):
    entity_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(CoreStore)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    converted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.SmallIntegerField(blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    is_multi_shipping = models.SmallIntegerField(blank=True, null=True)
    items_count = models.IntegerField(blank=True, null=True)
    items_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_order_id = models.IntegerField(blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_quote_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_currency_code = models.CharField(max_length=255, blank=True, null=True)
    store_currency_code = models.CharField(max_length=255, blank=True, null=True)
    quote_currency_code = models.CharField(max_length=255, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    checkout_method = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    customer_tax_class_id = models.IntegerField(blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_prefix = models.CharField(max_length=40, blank=True, null=True)
    customer_firstname = models.CharField(max_length=255, blank=True, null=True)
    customer_middlename = models.CharField(max_length=40, blank=True, null=True)
    customer_lastname = models.CharField(max_length=255, blank=True, null=True)
    customer_suffix = models.CharField(max_length=40, blank=True, null=True)
    customer_dob = models.DateTimeField(blank=True, null=True)
    customer_note = models.CharField(max_length=255, blank=True, null=True)
    customer_note_notify = models.SmallIntegerField(blank=True, null=True)
    customer_is_guest = models.SmallIntegerField(blank=True, null=True)
    remote_ip = models.CharField(max_length=255, blank=True, null=True)
    applied_rule_ids = models.CharField(max_length=255, blank=True, null=True)
    reserved_order_id = models.CharField(max_length=64, blank=True, null=True)
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    global_currency_code = models.CharField(max_length=255, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_quote_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    customer_taxvat = models.CharField(max_length=255, blank=True, null=True)
    customer_gender = models.CharField(max_length=255, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_with_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_with_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_changed = models.IntegerField(blank=True, null=True)
    trigger_recollect = models.SmallIntegerField()
    ext_shipping_info = models.TextField(blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    is_persistent = models.SmallIntegerField(blank=True, null=True)
    buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    ebizmarts_abandonedcart_counter = models.IntegerField()
    ebizmarts_abandonedcart_flag = models.IntegerField()
    jirafe_visitor_id = models.CharField(max_length=255, blank=True, null=True)
    jirafe_orig_visitor_id = models.CharField(max_length=255, blank=True, null=True)
    ebizmarts_abandonedcart_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote'


class SalesFlatQuoteAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    quote = models.ForeignKey(SalesFlatQuote)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer_id = models.IntegerField(blank=True, null=True)
    save_in_address_book = models.SmallIntegerField(blank=True, null=True)
    customer_address_id = models.IntegerField(blank=True, null=True)
    address_type = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    prefix = models.CharField(max_length=40, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=40, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=40, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    same_as_billing = models.SmallIntegerField()
    free_shipping = models.SmallIntegerField()
    collect_shipping_rates = models.SmallIntegerField()
    shipping_method = models.CharField(max_length=255, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal_with_discount = models.DecimalField(max_digits=12, decimal_places=4)
    base_subtotal_with_discount = models.DecimalField(max_digits=12, decimal_places=4)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4)
    customer_notes = models.TextField(blank=True, null=True)
    applied_taxes = models.TextField(blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)
    shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    vat_id = models.TextField(blank=True, null=True)
    vat_is_valid = models.SmallIntegerField(blank=True, null=True)
    vat_request_id = models.TextField(blank=True, null=True)
    vat_request_date = models.TextField(blank=True, null=True)
    vat_request_success = models.SmallIntegerField(blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_buckaroo_fee_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_address'


class SalesFlatQuoteAddressItem(models.Model):
    address_item_id = models.AutoField(primary_key=True)
    parent_item = models.ForeignKey('self', blank=True, null=True)
    quote_address = models.ForeignKey(SalesFlatQuoteAddress)
    quote_item = models.ForeignKey('SalesFlatQuoteItem')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    applied_rule_ids = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4)
    row_total_with_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    super_product_id = models.IntegerField(blank=True, null=True)
    parent_product_id = models.IntegerField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    free_shipping = models.IntegerField(blank=True, null=True)
    is_qty_decimal = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    no_discount = models.IntegerField(blank=True, null=True)
    tax_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_address_item'


class SalesFlatQuoteItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    quote = models.ForeignKey(SalesFlatQuote)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    product = models.ForeignKey(CatalogProductEntity, blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    parent_item = models.ForeignKey('self', blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    applied_rule_ids = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    free_shipping = models.SmallIntegerField()
    is_qty_decimal = models.SmallIntegerField(blank=True, null=True)
    no_discount = models.SmallIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    base_price = models.DecimalField(max_digits=12, decimal_places=4)
    custom_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4)
    row_total_with_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    base_tax_before_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_before_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    original_custom_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied = models.TextField(blank=True, null=True)
    weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_row_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_row_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orderspro_is_temporary = models.IntegerField(blank=True, null=True)
    ordersedit_is_temporary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_item'


class SalesFlatQuoteItemOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(SalesFlatQuoteItem)
    product_id = models.IntegerField()
    code = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_item_option'


class SalesFlatQuotePayment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    quote = models.ForeignKey(SalesFlatQuote)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    method = models.CharField(max_length=255, blank=True, null=True)
    cc_type = models.CharField(max_length=255, blank=True, null=True)
    cc_number_enc = models.CharField(max_length=255, blank=True, null=True)
    cc_last4 = models.CharField(max_length=255, blank=True, null=True)
    cc_cid_enc = models.CharField(max_length=255, blank=True, null=True)
    cc_owner = models.CharField(max_length=255, blank=True, null=True)
    cc_exp_month = models.SmallIntegerField(blank=True, null=True)
    cc_exp_year = models.SmallIntegerField(blank=True, null=True)
    cc_ss_owner = models.CharField(max_length=255, blank=True, null=True)
    cc_ss_start_month = models.SmallIntegerField(blank=True, null=True)
    cc_ss_start_year = models.SmallIntegerField(blank=True, null=True)
    po_number = models.CharField(max_length=255, blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    cc_ss_issue = models.CharField(max_length=255, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    paypal_payer_id = models.CharField(max_length=255, blank=True, null=True)
    paypal_payer_status = models.CharField(max_length=255, blank=True, null=True)
    paypal_correlation_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_payment'


class SalesFlatQuoteShippingRate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    address = models.ForeignKey(SalesFlatQuoteAddress)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    carrier = models.CharField(max_length=255, blank=True, null=True)
    carrier_title = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    method_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    error_message = models.TextField(blank=True, null=True)
    method_title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_shipping_rate'


class SalesFlatShipment(models.Model):
    entity_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    total_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    email_sent = models.SmallIntegerField(blank=True, null=True)
    order = models.ForeignKey(SalesFlatOrder)
    customer_id = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    shipment_status = models.IntegerField(blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    packages = models.TextField(blank=True, null=True)
    shipping_label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment'


class SalesFlatShipmentComment(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatShipment)
    is_customer_notified = models.IntegerField(blank=True, null=True)
    is_visible_on_front = models.SmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment_comment'


class SalesFlatShipmentGrid(models.Model):
    entity = models.ForeignKey(SalesFlatShipment, primary_key=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    total_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_id = models.IntegerField()
    shipment_status = models.IntegerField(blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    order_increment_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    order_created_at = models.DateTimeField(blank=True, null=True)
    shipping_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment_grid'


class SalesFlatShipmentItem(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatShipment)
    row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment_item'


class SalesFlatShipmentTrack(models.Model):
    entity_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(SalesFlatShipment)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_id = models.IntegerField()
    track_number = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    carrier_code = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment_track'


class SalesInvoicedAggregated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    orders_count = models.IntegerField()
    orders_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced_not_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_invoiced_aggregated'
        unique_together = (('period', 'store_id', 'order_status'),)


class SalesInvoicedAggregatedOrder(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    orders_count = models.IntegerField()
    orders_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced_not_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_invoiced_aggregated_order'
        unique_together = (('period', 'store_id', 'order_status'),)


class SalesOrderAggregatedCreated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    orders_count = models.IntegerField()
    total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    total_qty_invoiced = models.DecimalField(max_digits=12, decimal_places=4)
    total_income_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_revenue_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_profit_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_invoiced_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_canceled_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_paid_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_refunded_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_tax_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_shipping_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_discount_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'sales_order_aggregated_created'
        unique_together = (('period', 'store_id', 'order_status'),)


class SalesOrderAggregatedUpdated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    orders_count = models.IntegerField()
    total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    total_qty_invoiced = models.DecimalField(max_digits=12, decimal_places=4)
    total_income_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_revenue_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_profit_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_invoiced_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_canceled_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_paid_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_refunded_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_tax_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_shipping_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_discount_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'sales_order_aggregated_updated'
        unique_together = (('period', 'store_id', 'order_status'),)


class SalesOrderStatus(models.Model):
    status = models.CharField(primary_key=True, max_length=32)
    label = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'sales_order_status'


class SalesOrderStatusLabel(models.Model):
    status = models.ForeignKey(SalesOrderStatus, db_column='status')
    store = models.ForeignKey(CoreStore)
    label = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'sales_order_status_label'
        unique_together = (('status', 'store_id'),)


class SalesOrderStatusNotification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    status_code = models.CharField(max_length=100)
    store_id = models.IntegerField()
    template_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales_order_status_notification'
        unique_together = (('status_code', 'store_id'),)


class SalesOrderStatusState(models.Model):
    status = models.ForeignKey(SalesOrderStatus, db_column='status')
    state = models.CharField(max_length=32)
    is_default = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_order_status_state'
        unique_together = (('status', 'state'),)


class SalesOrderTax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    priority = models.IntegerField()
    position = models.IntegerField()
    base_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    process = models.SmallIntegerField()
    base_real_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_order_tax'


class SalesOrderTaxItem(models.Model):
    tax_item_id = models.AutoField(primary_key=True)
    tax = models.ForeignKey(SalesOrderTax)
    item = models.ForeignKey(SalesFlatOrderItem)
    tax_percent = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'sales_order_tax_item'
        unique_together = (('tax_id', 'item_id'),)


class SalesPaymentTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    order = models.ForeignKey(SalesFlatOrder)
    payment = models.ForeignKey(SalesFlatOrderPayment)
    txn_id = models.CharField(max_length=100, blank=True, null=True)
    parent_txn_id = models.CharField(max_length=100, blank=True, null=True)
    txn_type = models.CharField(max_length=15, blank=True, null=True)
    is_closed = models.SmallIntegerField()
    additional_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_payment_transaction'
        unique_together = (('order_id', 'payment_id', 'txn_id'),)


class SalesRecurringProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=20)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    method_code = models.CharField(max_length=32)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    reference_id = models.CharField(max_length=32, blank=True, null=True)
    subscriber_name = models.CharField(max_length=150, blank=True, null=True)
    start_datetime = models.DateTimeField()
    internal_reference_id = models.CharField(unique=True, max_length=42)
    schedule_description = models.CharField(max_length=255)
    suspension_threshold = models.SmallIntegerField(blank=True, null=True)
    bill_failed_later = models.SmallIntegerField()
    period_unit = models.CharField(max_length=20)
    period_frequency = models.SmallIntegerField(blank=True, null=True)
    period_max_cycles = models.SmallIntegerField(blank=True, null=True)
    billing_amount = models.DecimalField(max_digits=12, decimal_places=4)
    trial_period_unit = models.CharField(max_length=20, blank=True, null=True)
    trial_period_frequency = models.SmallIntegerField(blank=True, null=True)
    trial_period_max_cycles = models.SmallIntegerField(blank=True, null=True)
    trial_billing_amount = models.TextField(blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    init_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    init_may_fail = models.SmallIntegerField()
    order_info = models.TextField()
    order_item_info = models.TextField()
    billing_address_info = models.TextField()
    shipping_address_info = models.TextField(blank=True, null=True)
    profile_vendor_info = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_recurring_profile'


class SalesRecurringProfileOrder(models.Model):
    link_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(SalesRecurringProfile)
    order = models.ForeignKey(SalesFlatOrder)

    class Meta:
        managed = False
        db_table = 'sales_recurring_profile_order'
        unique_together = (('profile_id', 'order_id'),)


class SalesRefundedAggregated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    orders_count = models.IntegerField()
    refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_refunded_aggregated'
        unique_together = (('period', 'store_id', 'order_status'),)


class SalesRefundedAggregatedOrder(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    orders_count = models.IntegerField()
    refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_refunded_aggregated_order'
        unique_together = (('period', 'store_id', 'order_status'),)


class SalesShippingAggregated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    orders_count = models.IntegerField()
    total_shipping = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_shipping_actual = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_shipping_aggregated'
        unique_together = (('period', 'store_id', 'order_status', 'shipping_description'),)


class SalesShippingAggregatedOrder(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    orders_count = models.IntegerField()
    total_shipping = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_shipping_actual = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_shipping_aggregated_order'
        unique_together = (('period', 'store_id', 'order_status', 'shipping_description'),)


class Salesrule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    uses_per_customer = models.IntegerField()
    is_active = models.SmallIntegerField()
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)
    stop_rules_processing = models.SmallIntegerField()
    is_advanced = models.SmallIntegerField()
    product_ids = models.TextField(blank=True, null=True)
    sort_order = models.IntegerField()
    simple_action = models.CharField(max_length=32, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    discount_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_step = models.IntegerField()
    simple_free_shipping = models.SmallIntegerField()
    apply_to_shipping = models.SmallIntegerField()
    times_used = models.IntegerField()
    is_rss = models.SmallIntegerField()
    coupon_type = models.SmallIntegerField()
    use_auto_generation = models.SmallIntegerField()
    uses_per_coupon = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salesrule'


class SalesruleCoupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    rule = models.ForeignKey(Salesrule)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    usage_limit = models.IntegerField(blank=True, null=True)
    usage_per_customer = models.IntegerField(blank=True, null=True)
    times_used = models.IntegerField()
    expiration_date = models.DateTimeField(blank=True, null=True)
    is_primary = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    type = models.SmallIntegerField(blank=True, null=True)
    is_popup = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesrule_coupon'
        unique_together = (('rule_id', 'is_primary'),)


class SalesruleCouponUsage(models.Model):
    coupon = models.ForeignKey(SalesruleCoupon)
    customer = models.ForeignKey(CustomerEntity)
    times_used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salesrule_coupon_usage'
        unique_together = (('coupon_id', 'customer_id'),)


class SalesruleCustomer(models.Model):
    rule_customer_id = models.AutoField(primary_key=True)
    rule = models.ForeignKey(Salesrule)
    customer = models.ForeignKey(CustomerEntity)
    times_used = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'salesrule_customer'


class SalesruleCustomerGroup(models.Model):
    rule = models.ForeignKey(Salesrule)
    customer_group = models.ForeignKey(CustomerGroup)

    class Meta:
        managed = False
        db_table = 'salesrule_customer_group'
        unique_together = (('rule_id', 'customer_group_id'),)


class SalesruleLabel(models.Model):
    label_id = models.AutoField(primary_key=True)
    rule = models.ForeignKey(Salesrule)
    store = models.ForeignKey(CoreStore)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesrule_label'
        unique_together = (('rule_id', 'store_id'),)


class SalesruleProductAttribute(models.Model):
    rule = models.ForeignKey(Salesrule)
    website = models.ForeignKey(CoreWebsite)
    customer_group = models.ForeignKey(CustomerGroup)
    attribute = models.ForeignKey(EavAttribute)

    class Meta:
        managed = False
        db_table = 'salesrule_product_attribute'
        unique_together = (('rule_id', 'website_id', 'customer_group_id', 'attribute_id'),)


class SalesruleWebsite(models.Model):
    rule = models.ForeignKey(Salesrule)
    website = models.ForeignKey(CoreWebsite)

    class Meta:
        managed = False
        db_table = 'salesrule_website'
        unique_together = (('rule_id', 'website_id'),)


class SendfriendLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=16, blank=True, null=True)
    time = models.IntegerField()
    website_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sendfriend_log'


class ShippingTablerate(models.Model):
    pk = models.AutoField(primary_key=True)
    website_id = models.IntegerField()
    dest_country_id = models.CharField(max_length=4)
    dest_region_id = models.IntegerField()
    dest_zip = models.CharField(max_length=10)
    condition_name = models.CharField(max_length=20)
    condition_value = models.DecimalField(max_digits=12, decimal_places=4)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    cost = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'shipping_tablerate'
        unique_together = (('website_id', 'dest_country_id', 'dest_region_id', 'dest_zip', 'condition_name', 'condition_value'),)


class Sitemap(models.Model):
    sitemap_id = models.AutoField(primary_key=True)
    sitemap_type = models.CharField(max_length=32, blank=True, null=True)
    sitemap_filename = models.CharField(max_length=32, blank=True, null=True)
    sitemap_path = models.CharField(max_length=255, blank=True, null=True)
    sitemap_time = models.DateTimeField(blank=True, null=True)
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'sitemap'


class SmtpproEmailLog(models.Model):
    email_id = models.AutoField(primary_key=True)
    log_at = models.DateTimeField()
    email_to = models.CharField(max_length=255)
    template = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    email_body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smtppro_email_log'


class StaempfliProductattachmentFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    store_id = models.SmallIntegerField()
    filename = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sort_order = models.IntegerField()
    path = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staempfli_productattachment_file'


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField()
    first_customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    first_store = models.ForeignKey(CoreStore, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class TagProperties(models.Model):
    tag = models.ForeignKey(Tag)
    store = models.ForeignKey(CoreStore)
    base_popularity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tag_properties'
        unique_together = (('tag_id', 'store_id'),)


class TagRelation(models.Model):
    tag_relation_id = models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tag)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity)
    store = models.ForeignKey(CoreStore)
    active = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_relation'
        unique_together = (('tag_id', 'customer_id', 'product_id', 'store_id'),)


class TagSummary(models.Model):
    tag = models.ForeignKey(Tag)
    store = models.ForeignKey(CoreStore)
    customers = models.IntegerField()
    products = models.IntegerField()
    uses = models.IntegerField()
    historical_uses = models.IntegerField()
    popularity = models.IntegerField()
    base_popularity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tag_summary'
        unique_together = (('tag_id', 'store_id'),)


class TaxCalculation(models.Model):
    tax_calculation_id = models.AutoField(primary_key=True)
    tax_calculation_rate = models.ForeignKey('TaxCalculationRate')
    tax_calculation_rule = models.ForeignKey('TaxCalculationRule')
    customer_tax_class = models.ForeignKey('TaxClass')
    product_tax_class = models.ForeignKey('TaxClass')

    class Meta:
        managed = False
        db_table = 'tax_calculation'


class TaxCalculationRate(models.Model):
    tax_calculation_rate_id = models.AutoField(primary_key=True)
    tax_country_id = models.CharField(max_length=2)
    tax_region_id = models.IntegerField()
    tax_postcode = models.CharField(max_length=21, blank=True, null=True)
    code = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=12, decimal_places=4)
    zip_is_range = models.SmallIntegerField(blank=True, null=True)
    zip_from = models.IntegerField(blank=True, null=True)
    zip_to = models.IntegerField(blank=True, null=True)
    tax_ebvatcode = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_calculation_rate'


class TaxCalculationRateTitle(models.Model):
    tax_calculation_rate_title_id = models.AutoField(primary_key=True)
    tax_calculation_rate = models.ForeignKey(TaxCalculationRate)
    store = models.ForeignKey(CoreStore)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tax_calculation_rate_title'


class TaxCalculationRule(models.Model):
    tax_calculation_rule_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    priority = models.IntegerField()
    position = models.IntegerField()
    calculate_subtotal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_calculation_rule'


class TaxClass(models.Model):
    class_id = models.SmallIntegerField(primary_key=True)
    class_name = models.CharField(max_length=255)
    class_type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'tax_class'


class TaxOrderAggregatedCreated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    code = models.CharField(max_length=255)
    order_status = models.CharField(max_length=50)
    percent = models.FloatField(blank=True, null=True)
    orders_count = models.IntegerField()
    tax_base_amount_sum = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_order_aggregated_created'
        unique_together = (('period', 'store_id', 'code', 'percent', 'order_status'),)


class TaxOrderAggregatedUpdated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    code = models.CharField(max_length=255)
    order_status = models.CharField(max_length=50)
    percent = models.FloatField(blank=True, null=True)
    orders_count = models.IntegerField()
    tax_base_amount_sum = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_order_aggregated_updated'
        unique_together = (('period', 'store_id', 'code', 'percent', 'order_status'),)


class TigBuckarooGiftcard(models.Model):
    entity_id = models.AutoField(primary_key=True)
    servicecode = models.CharField(unique=True, max_length=255)
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tig_buckaroo_giftcard'


class TigMyparcelShipment(models.Model):
    entity_id = models.AutoField(primary_key=True)
    shipment = models.ForeignKey(SalesFlatShipment, unique=True, blank=True, null=True)
    order = models.ForeignKey(SalesFlatOrder, blank=True, null=True)
    consignment_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    shipment_type = models.CharField(max_length=16)
    status = models.CharField(max_length=64, blank=True, null=True)
    barcode = models.CharField(max_length=64, blank=True, null=True)
    home_address_only = models.IntegerField(blank=True, null=True)
    signature_on_receipt = models.IntegerField(blank=True, null=True)
    return_if_no_answer = models.IntegerField(blank=True, null=True)
    insured = models.IntegerField(blank=True, null=True)
    insured_amount = models.IntegerField(blank=True, null=True)
    is_final = models.IntegerField(blank=True, null=True)
    barcode_send = models.IntegerField(blank=True, null=True)
    retourlink = models.CharField(max_length=255, blank=True, null=True)
    is_credit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tig_myparcel_shipment'


class TmCoreModule(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    data_version = models.CharField(max_length=50, blank=True, null=True)
    identity_key = models.TextField(blank=True, null=True)
    store_ids = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'tm_core_module'


class TmEmailGatewayStorage(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.SmallIntegerField()
    type = models.SmallIntegerField()
    email = models.CharField(max_length=128)
    host = models.CharField(max_length=128)
    user = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    port = models.SmallIntegerField()
    secure = models.SmallIntegerField()
    remove = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tm_email_gateway_storage'


class TmEmailGatewayTransport(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.SmallIntegerField()
    type = models.SmallIntegerField()
    email = models.CharField(max_length=128)
    host = models.CharField(max_length=128)
    user = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    port = models.SmallIntegerField()
    secure = models.SmallIntegerField()
    auth = models.CharField(max_length=7)
    custom = models.TextField()

    class Meta:
        managed = False
        db_table = 'tm_email_gateway_transport'


class TmEmailQueueMessage(models.Model):
    message_id = models.BigIntegerField(primary_key=True)
    queue = models.ForeignKey('TmEmailQueueQueue')
    handle = models.CharField(unique=True, max_length=32, blank=True, null=True)
    body = models.TextField()
    md5 = models.CharField(max_length=32)
    status = models.SmallIntegerField()
    timeout = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tm_email_queue_message'


class TmEmailQueueQueue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    queue_name = models.CharField(max_length=100)
    default_status = models.SmallIntegerField()
    timeout = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tm_email_queue_queue'


class TmHelpmateDepartment(models.Model):
    active = models.IntegerField()
    name = models.CharField(max_length=45, blank=True, null=True)
    store = models.ForeignKey(CoreStore)
    default_user_id = models.IntegerField(blank=True, null=True)
    gateway = models.ForeignKey(TmEmailGatewayStorage, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    sender = models.CharField(max_length=32, blank=True, null=True)
    email_template_new = models.SmallIntegerField()
    email_template_answer = models.SmallIntegerField()
    email_template_admin = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tm_helpmate_department'


class TmHelpmateDepartmentUser(models.Model):
    department = models.ForeignKey(TmHelpmateDepartment)
    user = models.ForeignKey(AdminUser)

    class Meta:
        managed = False
        db_table = 'tm_helpmate_department_user'


class TmHelpmateStatus(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tm_helpmate_status'


class TmHelpmateTheard(models.Model):
    ticket = models.ForeignKey('TmHelpmateTicket')
    message_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(AdminUser, blank=True, null=True)
    status = models.IntegerField()
    priority = models.IntegerField()
    department = models.ForeignKey(TmHelpmateDepartment)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tm_helpmate_theard'


class TmHelpmateTicket(models.Model):
    number = models.CharField(max_length=32)
    customer = models.ForeignKey(CustomerEntity, blank=True, null=True)
    email = models.CharField(max_length=128)
    status = models.ForeignKey(TmHelpmateStatus, db_column='status')
    title = models.CharField(max_length=45, blank=True, null=True)
    priority = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    department = models.ForeignKey(TmHelpmateDepartment)
    user = models.ForeignKey(AdminUser, blank=True, null=True)
    store = models.ForeignKey(CoreStore)
    notes = models.TextField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    field0 = models.TextField(blank=True, null=True)
    field1 = models.TextField(blank=True, null=True)
    field2 = models.TextField(blank=True, null=True)
    visitor_id = models.IntegerField(blank=True, null=True)
    rate = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tm_helpmate_ticket'


class TmKnowledgebaseCategory(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    identifier = models.CharField(max_length=255)
    store = models.ForeignKey(CoreStore)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tm_knowledgebase_category'


class TmKnowledgebaseFaq(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    meta_keywords = models.TextField()
    meta_description = models.TextField()
    content = models.TextField(blank=True, null=True)
    identifier = models.CharField(max_length=255)
    author = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tm_knowledgebase_faq'


class TmKnowledgebaseFaqCategory(models.Model):
    faq_id = models.IntegerField()
    category = models.ForeignKey(TmKnowledgebaseCategory)

    class Meta:
        managed = False
        db_table = 'tm_knowledgebase_faq_category'


class TmKnowledgebaseFaqStore(models.Model):
    faq_id = models.IntegerField()
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'tm_knowledgebase_faq_store'


class VantageMessage(models.Model):
    message_id = models.BigIntegerField(primary_key=True)
    queue = models.ForeignKey('VantageQueue')
    handle = models.CharField(unique=True, max_length=32, blank=True, null=True)
    body = models.TextField()
    md5 = models.CharField(max_length=32)
    timeout = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vantage_message'


class VantageQueue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    queue_name = models.CharField(max_length=100)
    timeout = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'vantage_queue'


class WcubeNonceCache(models.Model):
    nonce = models.TextField(blank=True, null=True)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wCube_nonce_cache'


class WeeeDiscount(models.Model):
    entity = models.ForeignKey(CatalogProductEntity)
    website = models.ForeignKey(CoreWebsite)
    customer_group = models.ForeignKey(CustomerGroup)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'weee_discount'


class WeeeTax(models.Model):
    value_id = models.AutoField(primary_key=True)
    website = models.ForeignKey(CoreWebsite)
    entity = models.ForeignKey(CatalogProductEntity)
    country = models.ForeignKey(DirectoryCountry, db_column='country', blank=True, null=True)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    state = models.CharField(max_length=255)
    attribute = models.ForeignKey(EavAttribute)
    entity_type_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'weee_tax'


class Widget(models.Model):
    widget_id = models.AutoField(primary_key=True)
    widget_code = models.CharField(max_length=255, blank=True, null=True)
    widget_type = models.CharField(max_length=255, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'widget'


class WidgetInstance(models.Model):
    instance_id = models.AutoField(primary_key=True)
    instance_type = models.CharField(max_length=255, blank=True, null=True)
    package_theme = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    store_ids = models.CharField(max_length=255)
    widget_parameters = models.TextField(blank=True, null=True)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'widget_instance'


class WidgetInstancePage(models.Model):
    page_id = models.AutoField(primary_key=True)
    instance = models.ForeignKey(WidgetInstance)
    page_group = models.CharField(max_length=25, blank=True, null=True)
    layout_handle = models.CharField(max_length=255, blank=True, null=True)
    block_reference = models.CharField(max_length=255, blank=True, null=True)
    page_for = models.CharField(max_length=25, blank=True, null=True)
    entities = models.TextField(blank=True, null=True)
    page_template = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'widget_instance_page'


class WidgetInstancePageLayout(models.Model):
    page = models.ForeignKey(WidgetInstancePage)
    layout_update = models.ForeignKey(CoreLayoutUpdate)

    class Meta:
        managed = False
        db_table = 'widget_instance_page_layout'
        unique_together = (('layout_update_id', 'page_id'),)


class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity, unique=True)
    shared = models.SmallIntegerField()
    sharing_code = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist'


class WishlistItem(models.Model):
    wishlist_item_id = models.AutoField(primary_key=True)
    wishlist = models.ForeignKey(Wishlist)
    product = models.ForeignKey(CatalogProductEntity)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    added_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'wishlist_item'


class WishlistItemOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    wishlist_item = models.ForeignKey(WishlistItem)
    product_id = models.IntegerField()
    code = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist_item_option'


class WordpressAssociation(models.Model):
    assoc_id = models.AutoField(primary_key=True)
    type = models.ForeignKey('WordpressAssociationType')
    object_id = models.IntegerField()
    wordpress_object_id = models.IntegerField()
    position = models.IntegerField()
    store = models.ForeignKey(CoreStore)

    class Meta:
        managed = False
        db_table = 'wordpress_association'


class WordpressAssociationType(models.Model):
    type_id = models.AutoField(primary_key=True)
    object = models.CharField(max_length=16)
    wordpress_object = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'wordpress_association_type'


class WsaloggerLog(models.Model):
    notification_id = models.AutoField(primary_key=True)
    severity = models.IntegerField()
    date_added = models.DateTimeField()
    extension = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.IntegerField()
    is_remove = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wsalogger_log'


class XmlconnectApplication(models.Model):
    application_id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(unique=True, max_length=32)
    type = models.CharField(max_length=32)
    store = models.ForeignKey(CoreStore, blank=True, null=True)
    active_from = models.DateField(blank=True, null=True)
    active_to = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()
    browsing_mode = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xmlconnect_application'


class XmlconnectConfigData(models.Model):
    application = models.ForeignKey(XmlconnectApplication)
    category = models.CharField(max_length=60)
    path = models.CharField(max_length=250)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'xmlconnect_config_data'
        unique_together = (('application_id', 'category', 'path'),)


class XmlconnectHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(XmlconnectApplication)
    created_at = models.DateTimeField(blank=True, null=True)
    store_id = models.SmallIntegerField(blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200)
    activation_key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'xmlconnect_history'


class XmlconnectImages(models.Model):
    image_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(XmlconnectApplication)
    image_file = models.CharField(max_length=255)
    image_type = models.CharField(max_length=255)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xmlconnect_images'


class XmlconnectNotificationTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    push_title = models.CharField(max_length=140)
    message_title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    application = models.ForeignKey(XmlconnectApplication)

    class Meta:
        managed = False
        db_table = 'xmlconnect_notification_template'


class XmlconnectQueue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    exec_time = models.DateTimeField(blank=True, null=True)
    template = models.ForeignKey(XmlconnectNotificationTemplate)
    push_title = models.CharField(max_length=140)
    message_title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    type = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'xmlconnect_queue'


class XtcoreConfigData(models.Model):
    config_id = models.AutoField(primary_key=True)
    path = models.CharField(unique=True, max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'xtcore_config_data'
