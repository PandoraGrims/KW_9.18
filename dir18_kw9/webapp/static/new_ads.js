// public/js/new_ads.js
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.approve-btn').forEach(function (btn) {
        btn.onclick = function () {
            approveAd(btn.dataset.adId);
        }
    });

    document.querySelectorAll('.reject-btn').forEach(function (btn) {
        btn.onclick = function () {
            rejectAd(btn.dataset.adId);
        }
    });
});

function approveAd(adId) {
    // Отправить AJAX-запрос для одобрения объявления
    // Обновить интерфейс, если запрос успешен
}

function rejectAd(adId) {
    // Отправить AJAX-запрос для отклонения объявления
    // Обновить интерфейс, если запрос успешен
}
