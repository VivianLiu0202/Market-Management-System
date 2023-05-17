function goods_id(goodsId) {
    var input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('name', 'update_goods_id');
    input.setAttribute('value', goodsId);
    input.style.display = "none";
    document.getElementById(goodsId).appendChild(input);
    document.getElementById(goodsId).submit();
}