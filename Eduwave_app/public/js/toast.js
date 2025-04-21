setTimeout(() => {
    const toast = document.getElementById("toast-container");
    if (toast) {
        toast.style.opacity = "0";

        toast.addEventListener('transitionend', () => {
            toast.remove();
        });
    }
}, 8000); 