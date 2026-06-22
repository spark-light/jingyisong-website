/**
 * Common HTML Components for Jingyi Song Website
 * Encapsulated for reuse across static pages without CORS/build-step requirements.
 */

function getHeaderHTML(activePage) {
    return `
<nav class="navbar">
    <div class="nav-centered">
        <div class="nav-mobile-brand">
            <div class="hamburger" id="hamburger" aria-label="Toggle navigation">
                <span></span><span></span><span></span>
            </div>
            ${activePage === 'home' ? '' : `
            <a href="/" class="nav-brand-info">
                <span class="nav-brand-title">Jingyi Song 宋静宜</span>
                <span class="nav-brand-subtitle">Violist, Violin and Viola Teacher</span>
            </a>
            `}
        </div>
        <ul class="nav-links" id="navLinks">
            <li><a href="/" class="${activePage === 'home' ? 'active' : ''}">HOME/主页</a></li>
            <li><a href="/biography" class="${activePage === 'biography' ? 'active' : ''}">BIOGRAPHY/关于我</a></li>
            <li><a href="/gallery" class="${activePage === 'gallery' ? 'active' : ''}">GALLERY/照片</a></li>
            <li><a href="/contact" class="${activePage === 'contact' ? 'active' : ''}">CONTACT ME/联系我</a></li>
            <li><a href="/review" class="${activePage === 'review' ? 'active' : ''}">REVIEW/留言</a></li>
        </ul>
    </div>
</nav>
    `;
}

function getTaglineBannerHTML() {
    return `
<div class="section-container tagline-banner-container" style="padding-top: 2.5rem; padding-bottom: 0.5rem;">
    <div class="bio-hero-banner">
        <h1 class="bio-hero-name">Jingyi Song<span class="bio-hero-name-cn">宋静宜</span></h1>
        <p class="bio-hero-tagline">Violist, Violin and Viola Teacher</p>
    </div>
</div>
    `;
}

function getFooterHTML() {
    return `
<footer>
    <div class="footer-inner">
        <hr class="footer-divider-top">
        <div class="footer-social">
            <a href="https://www.youtube.com/@Jingyi_Song" target="_blank" rel="noopener" aria-label="YouTube Channel">
                <svg viewBox="0 0 24 24" fill="currentColor" style="color:#FF0000">
                    <path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10A10 10 0 0012 2z"/>
                    <path fill-rule="evenodd" fill="#fff" d="M17.607 14.302s.066-.931.066-1.866l.003-.88c0-.93-.069-1.865-.069-1.865a2.363 2.363 0 00-.436-1.146 1.702 1.702 0 00-1.16-.52c-1.615-.116-4.025-.149-4.025-.149s-2.422.033-4.037.15c-.436.012-.85.193-1.156.505-.335.349-.364 1.153-.364 1.153s-.033.942-.033 1.876v.884c0 .93.033 1.865.033 1.865.033.413.177.809.418 1.146.344.31.788.484 1.251.49.924.088 3.913.117 3.913.117s2.418-.004 4.033-.12c.433-.004.847-.18 1.152-.488.242-.338.384-.737.411-1.152zm-3.68-2.422l-3.116 1.614-.004-3.24 3.12 1.626z"/>
                </svg>
            </a>
        </div>
        <p class="footer-copy">Copyright © 2026 Jingyi Song All Rights Reserved</p>
    </div>
</footer>
    `;
}
