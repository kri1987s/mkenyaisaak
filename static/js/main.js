document.addEventListener('DOMContentLoaded', function () {
    // Countdown Timer Function
    const initCountdown = (elementId) => {
        const countdownContainer = document.getElementById(elementId);
        if (countdownContainer) {
            const targetDateStr = countdownContainer.getAttribute('data-target-date');
            if (targetDateStr) {
                const targetDate = new Date(targetDateStr).getTime();

                const updateCountdown = () => {
                    const now = new Date().getTime();
                    const distance = targetDate - now;

                    if (distance < 0) {
                        countdownContainer.innerHTML = "<div class='h3 text-warning'>EVENT STARTED</div>";
                        return;
                    }

                    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
                    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

                    // Update specific elements
                    const dayEl = countdownContainer.querySelector('[data-unit="days"]');
                    const hourEl = countdownContainer.querySelector('[data-unit="hours"]');
                    const minEl = countdownContainer.querySelector('[data-unit="minutes"]');
                    const secEl = countdownContainer.querySelector('[data-unit="seconds"]');

                    if (dayEl) dayEl.innerText = days < 10 ? "0" + days : days;
                    if (hourEl) hourEl.innerText = hours < 10 ? "0" + hours : hours;
                    if (minEl) minEl.innerText = minutes < 10 ? "0" + minutes : minutes;
                    if (secEl) secEl.innerText = seconds < 10 ? "0" + seconds : seconds;
                };

                setInterval(updateCountdown, 1000);
                updateCountdown();
            }
        }
    };

    // Initialize countdowns
    initCountdown('hero-countdown');
    initCountdown('event-countdown');
});

// Video Modal Logic
function openVideoModal(platform, embedUrl, embedCode) {
    const modalContent = document.getElementById('videoModalContent');
    const modal = new bootstrap.Modal(document.getElementById('videoModal'));

    let content = '';

    if (embedCode) {
        content = embedCode;
    } else if (platform === 'youtube') {
        content = `<iframe width="100%" height="100%" src="${embedUrl}?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="aspect-ratio: 16/9;"></iframe>`;
    } else if (platform === 'tiktok') {
        // TikTok embeds are tricky in modals due to script reloading. 
        // Best to link out or use specific iframe if available.
        // For now, we'll try to use the embed code if provided, or a link.
        content = `<div class="text-center text-white">
            <p>TikTok videos are best viewed on their app.</p>
            <a href="${embedUrl}" target="_blank" class="btn btn-primary">Watch on TikTok</a>
        </div>`;
    } else {
        content = `<div class="text-center text-white">
            <p>Content loading...</p>
            <a href="${embedUrl}" target="_blank" class="btn btn-primary">View Original</a>
        </div>`;
    }

    modalContent.innerHTML = content;
    modal.show();

    // Clear content on close to stop audio
    document.getElementById('videoModal').addEventListener('hidden.bs.modal', function () {
        modalContent.innerHTML = '';
    });
}
