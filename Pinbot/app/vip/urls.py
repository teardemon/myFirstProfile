# coding: utf-8

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import (
    VipRoleInfo,
    AlipayReturn,
    AlipayNotify,
    AlipayResult,
    ApplyRole,
    CreateOrder,
    OrderPaymentTerms,
    ApplyUserVip,
    OldPkgInfo,
    DownloadPDFView,
    Withdraw,
    WithdrawOperation,
    DisableUserVip,
)

from .vip_views.order_views import (
    CoinOrderInfo,
    PointOrderInfo,
    ManualServiceOrderInfo,
    SelfOrderInfo,
    CreateUserOrder,
    GetUserOrderList,
    GetSelfServiceSelect,
    GetManualServiceSelect,
    CoinPaidOrder,
    CloseOrder,
    CancelOrder,
    RefundOrder,
    CancelRefundOrder,
    ConfirmRefundOrder,
    ApplyUserManualService,
    OrderAlipayReturn,
    OrderAlipayNotify,
    OrderAlipayResult,
    Repaid,
    GetOrderStatus,
    GetCurrentUserInfo,
    OfflinePaySuccess,
    OrderPreRefund,
    GetSelfServiceSelectExample,
    GetManualServiceSelectExample,
    VipRoleInfoExample
)

from .vip_views.admin_views import (
    ConfirmRefundManualService,
    FinishedManualService,
    InvalidManualService,
    AdminOrderPage,
    AdminCreateOrder,
)

from .vip_views import self_views

from pin_utils.xadmin_utils import XAdminOperationForm

urlpatterns = patterns(
    '',
    url(
        r'^old_pkg_info/$',
        OldPkgInfo.as_view(),
        name='vip-old-pkg-info',
    ),
    url(
        r'^role_info/$',
        VipRoleInfo.as_view(),
        name='vip-role-info',
    ),
    url(
        r'^role_info_example/$',
        VipRoleInfoExample.as_view(),
        name='vip-role-info-example',
    ),
    url(
        r'^alipay_return/$',
        AlipayReturn.as_view(),
        name='vip-alipay-return',
    ),
    url(
        r'^alipay_notify/$',
        AlipayNotify.as_view(),
        name='vip-alipay-notify',
    ),
    url(
        r'^alipay_result/(?P<order_id>\d+)/$',
        AlipayResult.as_view(),
        name='vip-alipay-result',
    ),
    url(
        r'^apply_role/(?P<role_id>\d+)/$',
        ApplyRole.as_view(),
        name='vip-apply-role',
    ),
    url(
        r'^create_order/$',
        CreateOrder.as_view(),
        name='vip-create-order',
    ),
    url(
        r'^select_payway/$',
        OrderPaymentTerms.as_view(),
        name='vip-select-payway',
    ),
    url(
        r'^offline_pay_form/(?P<op_id>.+)/$',
        XAdminOperationForm.as_view(
            template='vip_offline_pay_form.html'
        ),
        name='vip-offline-pay-form',
    ),
    url(
        r'^offline_pay_success/(?P<order_id>.+)/$',
        OfflinePaySuccess.as_view(),
        name='vip-offline-pay-success',
    ),
    url(
        r'^apply_user_vip_form/(?P<op_id>.+)/$',
        XAdminOperationForm.as_view(
            template='apply_user_vip_form.html',
        ),
        name='vip-apply-user-vip-form',
    ),
    url(
        r'^apply_user_vip/(?P<vip_id>\d+)/$',
        ApplyUserVip.as_view(),
        name='vip-apply-user-vip',
    ),
    url(
        r'^vip_upgrade/$',
        VipRoleInfo.as_view(
            template_name='vip_upgrade.html'
        ),
        name='vip-upgrade-info',
    ),
    url(
        r'^vip_payment/$',
        OrderPaymentTerms.as_view(
            template_name='vip_payment.html'
        ),
        name='vip-upgrade-payment',
    ),
    url(
        r'^service_contact/$',
        TemplateView.as_view(template_name='service_contact.html'),
        name='service-contact',
    ),
    url(
        r'^download_contact/(?P<vip_id>\d+)/$',
        DownloadPDFView.as_view(
            template_name='service_contact.html'
        ),
        name='vip-service-contact',
    ),
    url(
        r'^withdraw/$',
        Withdraw.as_view(),
        name='vip-withdraw',
    ),
    url(
        r'^withdraw_form/(?P<op_id>\d+)/$',
        XAdminOperationForm.as_view(
            template='vip_withdraw_form.html',
        ),
        name='vip-withdraw-form',
    ),
    url(
        r'^withdraw_operation/(?P<record_id>\d+)/$',
        WithdrawOperation.as_view(),
        name='vip-withdraw-operation',
    ),
    url(
        r'^user_vip/disable_form/(?P<op_id>\d+)/$',
        XAdminOperationForm.as_view(
            template='disable_user_vip_form.html',
        ),
        name='vip-disable-form',
    ),
    url(
        r'^user_vip/disable/(?P<vip_id>\d+)/$',
        DisableUserVip.as_view(),
        name='vip-disable',
    ),
    url(
        r'^create_user_order/$',
        CreateUserOrder.as_view(),
        name='vip-create-user-order',
    ),
    url(
        r'^get_user_order_list/(?P<order_status>\w+)/$',
        GetUserOrderList.as_view(),
        name='vip-get-user-order-list',
    ),
    url(
        r'^apply_user_manual_service_form/(?P<op_id>.+)/$',
        XAdminOperationForm.as_view(
            template='apply_user_manual_service_form.html',
        ),
        name='vip-apply-user-manual-service-form',
    ),
    url(
        r'^apply_user_manual_service/(?P<manual_service_id>\d+)/$',
        ApplyUserManualService.as_view(),
        name='vip-apply-user-manual-service',
    ),
    url(
        r'^get_self_service_select/$',
        GetSelfServiceSelect.as_view(),
        name='vip-get-self-service-select',
    ),
    url(
        r'^get_self_service_select_example/$',
        GetSelfServiceSelectExample.as_view(),
        name='vip-get-self-service-select-example',
    ),
    url(
        r'^get_manual_service_select/$',
        GetManualServiceSelect.as_view(),
        name='vip-get-manual-service-select',
    ),
    url(
        r'^get_manual_service_select_example/$',
        GetManualServiceSelectExample.as_view(),
        name='vip-get-manual-service-select-example',
    ),

    url(
        r'^coin/info/$',
        CoinOrderInfo.as_view(),
        name='vip-coin-order-info',
    ),
    url(
        r'^point/info/$',
        PointOrderInfo.as_view(),
        name='vip-point-order-info',
    ),
    url(
        r'^manual/info/$',
        ManualServiceOrderInfo.as_view(),
        name='vip-manual-order-info',
    ),
    url(
        r'^self/info/$',
        SelfOrderInfo.as_view(),
        name='vip-self-order-info',
    ),
    url(
        r'^coin_paid_order/$',
        CoinPaidOrder.as_view(),
        name='vip-coin-paid-order',
    ),
    url(
        r'^order/close/$',
        CloseOrder.as_view(),
        name='vip-close-order',
    ),
    url(
        r'^order/cancel/$',
        CancelOrder.as_view(),
        name='vip-cancel-order',
    ),
    url(
        r'^order/refund/$',
        RefundOrder.as_view(),
        name='vip-refund-order',
    ),
    url(
        r'^order/cancel_refund/$',
        CancelRefundOrder.as_view(),
        name='vip-calcel-refund-order',
    ),
    url(
        r'^order/refund_form/(?P<op_id>.+)/$',
        XAdminOperationForm.as_view(
            template='order_refund_form.html',
        ),
        name='order-refund-form',
    ),
    url(
        r'^order/confirm_refund/(?P<op_id>.+)/$',
        ConfirmRefundOrder.as_view(),
        name='vip-confirm-refund-order',
    ),
    url(
        r'^manual_service_refund_form/(?P<op_id>.+)/$',
        XAdminOperationForm.as_view(
            template='manual_service_refund_form.html',
        ),
        name='vip-refund-manual-service-form',
    ),

    url(
        r'^manual_service_invalid_form/(?P<op_id>.+)/$',
        XAdminOperationForm.as_view(
            template='manual_service_invalid_form.html',
        ),
        name='vip-invalid-manual-service-form',
    ),

    url(
        r'^manual_service/confirm_refund/(?P<op_id>.+)/$',
        ConfirmRefundManualService.as_view(),
        name='manual-service-confirm-refund',
    ),
    url(
        r'^order/alipay_return/$',
        OrderAlipayReturn.as_view(),
        name='order-alipay-return',
    ),
    url(
        r'^order/alipay_notify/$',
        OrderAlipayNotify.as_view(),
        name='order-alipay-notify',
    ),
    url(
        r'^order/alipay_result/$',
        OrderAlipayResult.as_view(),
        name='order-alipay-result',
    ),
    url(
        r'^order/admin_page/$',
        AdminOrderPage.as_view(),
        name='order-admin-page',
    ),
    url(
        r'^order/admin_create/$',
        AdminCreateOrder.as_view(),
        name='order-admin-create',
    ),
    url(
        r'^manual_service/finished_form/(?P<op_id>.+)/$',
        FinishedManualService.as_view(),
        name='manual-service-finished',
    ),
    url(
        r'^manual_service/invalid_form/(?P<op_id>.+)/$',
        InvalidManualService.as_view(),
        name='manual-service-invalid',
    ),
    url(
        r'^manual_service_finished_form/(?P<op_id>.+)/$',
        XAdminOperationForm.as_view(
            template='manual_service_finished_form.html',
        ),
        name='vip-finished-manual-service-form',
    ),
    url(
        r'^order/repaid/$',
        Repaid.as_view(),
        name='vip-repaid-order',
    ),
    url(
        r'^order/get_order_status/$',
        GetOrderStatus.as_view(),
        name='vip-get-order-status',
    ),
    url(
        r'^get_user_info/$',
        GetCurrentUserInfo.as_view(),
        name='vip-get-user-info',
    ),
    # 账户过期提示页面
    url(
        r'^user_expired/$',
        login_required(TemplateView.as_view(
            template_name='user_expired.html'
        )),
        name='vip-user-expired',
    ),
    url(
        r'^order/pre_refund/(?P<service_id>.+)/$',
        OrderPreRefund.as_view(),
        name='vip-get-order-pre-refund',
    ),
    url(
        r'^self_service/list/$',
        self_views.SelfServiceList.as_view(),
        name='vip-self-service-list',
    ),
)
