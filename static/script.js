const productsContainer = document.getElementById('products');
const cartContainer = document.getElementById('cart');

const addToCart = (productId) => {
    fetch(`/add_to_cart/${productId}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                loadProducts();
                loadCart();
            }
        });
};

const loadProducts = () => {
    fetch('/products')
        .then(response => response.json())
        .then(products => {
            console.log(products);
            productsContainer.innerHTML = '';
            products.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('product');
                productDiv.innerHTML = `
                    <h3>${product.name}</h3>
                    <p>Type: ${product.type}</p>
                    <p>Price: $${parseFloat(product.price)}</p>
                    <p>Stock: ${product.stock_quantity}</p>
                    <button onclick="addToCart(${product.id})">Add to Cart</button>
                `;
                productsContainer.appendChild(productDiv);
            });
        });
};


const loadCart = () => {
    fetch('/cart')
        .then(response => response.json())
        .then(cartItems => {
            cartContainer.innerHTML = '';
            cartItems.forEach(item => {
                const cartItemDiv = document.createElement('div');
                cartItemDiv.classList.add('product', 'cart-item');
                cartItemDiv.innerHTML = `
                    <h3>${item.name}</h3>
                    <p>Quantity: ${item.quantity}</p>
                `;
                cartContainer.appendChild(cartItemDiv);
            });
        });
};


loadProducts();
loadCart();

