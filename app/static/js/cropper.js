/*!
 * Cropper v2.3.0
 * https://github.com/fengyuanchen/cropper
 *
 * Copyright (c) 2014-2016 Fengyuan Chen and contributors
 * Released under the MIT license
 *
 * Date: 2016-02-22T02:13:13.332Z
 */
!function (t) {
    "function" == typeof define && define.amd ? define(["jquery"], t) : t("object" == typeof exports ? require("jquery") : jQuery)
}(function (t) {
    "use strict";
    function i(t) {
        return "number" == typeof t && !isNaN(t)
    }

    function e(t) {
        return "undefined" == typeof t
    }

    function s(t, e) {
        var s = [];
        return i(e) && s.push(e), s.slice.apply(t, s)
    }

    function a(t, i) {
        var e = s(arguments, 2);
        return function () {
            return t.apply(i, e.concat(s(arguments)))
        }
    }

    function o(t) {
        var i = t.match(/^(https?:)\/\/([^\:\/\?#]+):?(\d*)/i);
        return i && (i[1] !== C.protocol || i[2] !== C.hostname || i[3] !== C.port)
    }

    function h(t) {
        var i = "timestamp=" + (new Date).getTime();
        return t + (-1 === t.indexOf("?") ? "?" : "&") + i
    }

    function n(t) {
        return t ? ' crossOrigin="' + t + '"' : ""
    }

    function r(t, i) {
        var e;
        return t.naturalWidth && !mt ? i(t.naturalWidth, t.naturalHeight) : (e = document.createElement("img"), e.onload = function () {
            i(this.width, this.height)
        }, void(e.src = t.src))
    }

    function p(t) {
        var e = [], s = t.rotate, a = t.scaleX, o = t.scaleY;
        return i(s) && e.push("rotate(" + s + "deg)"), i(a) && i(o) && e.push("scale(" + a + "," + o + ")"), e.length ? e.join(" ") : "none"
    }

    function l(t, i) {
        var e, s, a = Ct(t.degree) % 180, o = (a > 90 ? 180 - a : a) * Math.PI / 180, h = bt(o), n = Bt(o), r = t.width, p = t.height, l = t.aspectRatio;
        return i ? (e = r / (n + h / l), s = e / l) : (e = r * n + p * h, s = r * h + p * n), {width: e, height: s}
    }

    function c(e, s) {
        var a, o, h, n = t("<canvas>")[0], r = n.getContext("2d"), p = 0, c = 0, d = s.naturalWidth, g = s.naturalHeight, u = s.rotate, f = s.scaleX, m = s.scaleY, v = i(f) && i(m) && (1 !== f || 1 !== m), w = i(u) && 0 !== u, x = w || v, C = d * Ct(f || 1), b = g * Ct(m || 1);
        return v && (a = C / 2, o = b / 2), w && (h = l({
            width: C,
            height: b,
            degree: u
        }), C = h.width, b = h.height, a = C / 2, o = b / 2), n.width = C, n.height = b, x && (p = -d / 2, c = -g / 2, r.save(), r.translate(a, o)), w && r.rotate(u * Math.PI / 180), v && r.scale(f, m), r.drawImage(e, $t(p), $t(c), $t(d), $t(g)), x && r.restore(), n
    }

    function d(i) {
        var e = i.length, s = 0, a = 0;
        return e && (t.each(i, function (t, i) {
            s += i.pageX, a += i.pageY
        }), s /= e, a /= e), {pageX: s, pageY: a}
    }

    function g(t, i, e) {
        var s, a = "";
        for (s = i, e += i; e > s; s++)a += Lt(t.getUint8(s));
        return a
    }

    function u(t) {
        var i, e, s, a, o, h, n, r, p, l, c = new D(t), d = c.byteLength;
        if (255 === c.getUint8(0) && 216 === c.getUint8(1))for (p = 2; d > p;) {
            if (255 === c.getUint8(p) && 225 === c.getUint8(p + 1)) {
                n = p;
                break
            }
            p++
        }
        if (n && (e = n + 4, s = n + 10, "Exif" === g(c, e, 4) && (h = c.getUint16(s), o = 18761 === h, (o || 19789 === h) && 42 === c.getUint16(s + 2, o) && (a = c.getUint32(s + 4, o), a >= 8 && (r = s + a)))), r)for (d = c.getUint16(r, o), l = 0; d > l; l++)if (p = r + 12 * l + 2, 274 === c.getUint16(p, o)) {
            p += 8, i = c.getUint16(p, o), mt && c.setUint16(p, 1, o);
            break
        }
        return i
    }

    function f(t) {
        var i, e = t.replace(G, ""), s = atob(e), a = s.length, o = new B(a), h = new y(o);
        for (i = 0; a > i; i++)h[i] = s.charCodeAt(i);
        return o
    }

    function m(t) {
        var i, e = new y(t), s = e.length, a = "";
        for (i = 0; s > i; i++)a += Lt(e[i]);
        return "data:image/jpeg;base64," + $(a)
    }

    function v(i, e) {
        this.$element = t(i), this.options = t.extend({}, v.DEFAULTS, t.isPlainObject(e) && e), this.isLoaded = !1, this.isBuilt = !1, this.isCompleted = !1, this.isRotated = !1, this.isCropped = !1, this.isDisabled = !1, this.isReplaced = !1, this.isLimited = !1, this.wheeling = !1, this.isImg = !1, this.originalUrl = "", this.canvas = null, this.cropBox = null, this.init()
    }

    var w = t(window), x = t(document), C = window.location, b = window.navigator, B = window.ArrayBuffer, y = window.Uint8Array, D = window.DataView, $ = window.btoa, L = "cropper", T = "cropper-modal", X = "cropper-hide", Y = "cropper-hidden", k = "cropper-invisible", M = "cropper-move", W = "cropper-crop", H = "cropper-disabled", R = "cropper-bg", z = "mousedown touchstart pointerdown MSPointerDown", O = "mousemove touchmove pointermove MSPointerMove", E = "mouseup touchend touchcancel pointerup pointercancel MSPointerUp MSPointerCancel", P = "wheel mousewheel DOMMouseScroll", U = "dblclick", I = "load." + L, F = "error." + L, j = "resize." + L, A = "build." + L, S = "built." + L, N = "cropstart." + L, _ = "cropmove." + L, q = "cropend." + L, Z = "crop." + L, K = "zoom." + L, Q = /e|w|s|n|se|sw|ne|nw|all|crop|move|zoom/, V = /^data\:/, G = /^data\:([^\;]+)\;base64,/, J = /^data\:image\/jpeg.*;base64,/, tt = "preview", it = "action", et = "e", st = "w", at = "s", ot = "n", ht = "se", nt = "sw", rt = "ne", pt = "nw", lt = "all", ct = "crop", dt = "move", gt = "zoom", ut = "none", ft = t.isFunction(t("<canvas>")[0].getContext), mt = b && /safari/i.test(b.userAgent) && /apple computer/i.test(b.vendor), vt = Number, wt = Math.min, xt = Math.max, Ct = Math.abs, bt = Math.sin, Bt = Math.cos, yt = Math.sqrt, Dt = Math.round, $t = Math.floor, Lt = String.fromCharCode;
    v.prototype = {
        constructor: v, init: function () {
            var t, i = this.$element;
            if (i.is("img")) {
                if (this.isImg = !0, this.originalUrl = t = i.attr("src"), !t)return;
                t = i.prop("src")
            } else i.is("canvas") && ft && (t = i[0].toDataURL());
            this.load(t)
        }, trigger: function (i, e) {
            var s = t.Event(i, e);
            return this.$element.trigger(s), s
        }, load: function (i) {
            var e, s, a = this.options, o = this.$element;
            if (i && (o.one(A, a.build), !this.trigger(A).isDefaultPrevented())) {
                if (this.url = i, this.image = {}, !a.checkOrientation || !B)return this.clone();
                if (e = t.proxy(this.read, this), V.test(i))return J.test(i) ? e(f(i)) : this.clone();
                s = new XMLHttpRequest, s.onerror = s.onabort = t.proxy(function () {
                    this.clone()
                }, this), s.onload = function () {
                    e(this.response)
                }, s.open("get", i), s.responseType = "arraybuffer", s.send()
            }
        }, read: function (t) {
            var i, e, s, a = this.options, o = u(t), h = this.image;
            if (o > 1)switch (this.url = m(t), o) {
                case 2:
                    e = -1;
                    break;
                case 3:
                    i = -180;
                    break;
                case 4:
                    s = -1;
                    break;
                case 5:
                    i = 90, s = -1;
                    break;
                case 6:
                    i = 90;
                    break;
                case 7:
                    i = 90, e = -1;
                    break;
                case 8:
                    i = -90
            }
            a.rotatable && (h.rotate = i), a.scalable && (h.scaleX = e, h.scaleY = s), this.clone()
        }, clone: function () {
            var i, e, s = this.options, a = this.$element, r = this.url, p = "";
            s.checkCrossOrigin && o(r) && (p = a.prop("crossOrigin"), p ? i = r : (p = "anonymous", i = h(r))), this.crossOrigin = p, this.crossOriginUrl = i, this.$clone = e = t("<img" + n(p) + ' src="' + (i || r) + '">'), this.isImg ? a[0].complete ? this.start() : a.one(I, t.proxy(this.start, this)) : e.one(I, t.proxy(this.start, this)).one(F, t.proxy(this.stop, this)).addClass(X).insertAfter(a)
        }, start: function () {
            var i = this.$element, e = this.$clone;
            this.isImg || (e.off(F, this.stop), i = e), r(i[0], t.proxy(function (i, e) {
                t.extend(this.image, {
                    naturalWidth: i,
                    naturalHeight: e,
                    aspectRatio: i / e
                }), this.isLoaded = !0, this.build()
            }, this))
        }, stop: function () {
            this.$clone.remove(), this.$clone = null
        }, build: function () {
            var i, e, s, a = this.options, o = this.$element, h = this.$clone;
            this.isLoaded && (this.isBuilt && this.unbuild(), this.$container = o.parent(), this.$cropper = i = t(v.TEMPLATE), this.$canvas = i.find(".cropper-canvas").append(h), this.$dragBox = i.find(".cropper-drag-box"), this.$cropBox = e = i.find(".cropper-crop-box"), this.$viewBox = i.find(".cropper-view-box"), this.$face = s = e.find(".cropper-face"), o.addClass(Y).after(i), this.isImg || h.removeClass(X), this.initPreview(), this.bind(), a.aspectRatio = xt(0, a.aspectRatio) || NaN, a.viewMode = xt(0, wt(3, Dt(a.viewMode))) || 0, a.autoCrop ? (this.isCropped = !0, a.modal && this.$dragBox.addClass(T)) : e.addClass(Y), a.guides || e.find(".cropper-dashed").addClass(Y), a.center || e.find(".cropper-center").addClass(Y), a.cropBoxMovable && s.addClass(M).data(it, lt), a.highlight || s.addClass(k), a.background && i.addClass(R), a.cropBoxResizable || e.find(".cropper-line, .cropper-point").addClass(Y), this.setDragMode(a.dragMode), this.render(), this.isBuilt = !0, this.setData(a.data), o.one(S, a.built), setTimeout(t.proxy(function () {
                this.trigger(S), this.isCompleted = !0
            }, this), 0))
        }, unbuild: function () {
            this.isBuilt && (this.isBuilt = !1, this.isCompleted = !1, this.initialImage = null, this.initialCanvas = null, this.initialCropBox = null, this.container = null, this.canvas = null, this.cropBox = null, this.unbind(), this.resetPreview(), this.$preview = null, this.$viewBox = null, this.$cropBox = null, this.$dragBox = null, this.$canvas = null, this.$container = null, this.$cropper.remove(), this.$cropper = null)
        }, render: function () {
            this.initContainer(), this.initCanvas(), this.initCropBox(), this.renderCanvas(), this.isCropped && this.renderCropBox()
        }, initContainer: function () {
            var t = this.options, i = this.$element, e = this.$container, s = this.$cropper;
            s.addClass(Y), i.removeClass(Y), s.css(this.container = {
                width: xt(e.width(), vt(t.minContainerWidth) || 200),
                height: xt(e.height(), vt(t.minContainerHeight) || 100)
            }), i.addClass(Y), s.removeClass(Y)
        }, initCanvas: function () {
            var i, e = this.options.viewMode, s = this.container, a = s.width, o = s.height, h = this.image, n = h.naturalWidth, r = h.naturalHeight, p = 90 === Ct(h.rotate), l = p ? r : n, c = p ? n : r, d = l / c, g = a, u = o;
            o * d > a ? 3 === e ? g = o * d : u = a / d : 3 === e ? u = a / d : g = o * d, i = {
                naturalWidth: l,
                naturalHeight: c,
                aspectRatio: d,
                width: g,
                height: u
            }, i.oldLeft = i.left = (a - g) / 2, i.oldTop = i.top = (o - u) / 2, this.canvas = i, this.isLimited = 1 === e || 2 === e, this.limitCanvas(!0, !0), this.initialImage = t.extend({}, h), this.initialCanvas = t.extend({}, i)
        }, limitCanvas: function (t, i) {
            var e, s, a, o, h = this.options, n = h.viewMode, r = this.container, p = r.width, l = r.height, c = this.canvas, d = c.aspectRatio, g = this.cropBox, u = this.isCropped && g;
            t && (e = vt(h.minCanvasWidth) || 0, s = vt(h.minCanvasHeight) || 0, n && (n > 1 ? (e = xt(e, p), s = xt(s, l), 3 === n && (s * d > e ? e = s * d : s = e / d)) : e ? e = xt(e, u ? g.width : 0) : s ? s = xt(s, u ? g.height : 0) : u && (e = g.width, s = g.height, s * d > e ? e = s * d : s = e / d)), e && s ? s * d > e ? s = e / d : e = s * d : e ? s = e / d : s && (e = s * d), c.minWidth = e, c.minHeight = s, c.maxWidth = 1 / 0, c.maxHeight = 1 / 0), i && (n ? (a = p - c.width, o = l - c.height, c.minLeft = wt(0, a), c.minTop = wt(0, o), c.maxLeft = xt(0, a), c.maxTop = xt(0, o), u && this.isLimited && (c.minLeft = wt(g.left, g.left + g.width - c.width), c.minTop = wt(g.top, g.top + g.height - c.height), c.maxLeft = g.left, c.maxTop = g.top, 2 === n && (c.width >= p && (c.minLeft = wt(0, a), c.maxLeft = xt(0, a)), c.height >= l && (c.minTop = wt(0, o), c.maxTop = xt(0, o))))) : (c.minLeft = -c.width, c.minTop = -c.height, c.maxLeft = p, c.maxTop = l))
        }, renderCanvas: function (t) {
            var i, e, s = this.canvas, a = this.image, o = a.rotate, h = a.naturalWidth, n = a.naturalHeight;
            this.isRotated && (this.isRotated = !1, e = l({
                width: a.width,
                height: a.height,
                degree: o
            }), i = e.width / e.height, i !== s.aspectRatio && (s.left -= (e.width - s.width) / 2, s.top -= (e.height - s.height) / 2, s.width = e.width, s.height = e.height, s.aspectRatio = i, s.naturalWidth = h, s.naturalHeight = n, o % 180 && (e = l({
                width: h,
                height: n,
                degree: o
            }), s.naturalWidth = e.width, s.naturalHeight = e.height), this.limitCanvas(!0, !1))), (s.width > s.maxWidth || s.width < s.minWidth) && (s.left = s.oldLeft), (s.height > s.maxHeight || s.height < s.minHeight) && (s.top = s.oldTop), s.width = wt(xt(s.width, s.minWidth), s.maxWidth), s.height = wt(xt(s.height, s.minHeight), s.maxHeight), this.limitCanvas(!1, !0), s.oldLeft = s.left = wt(xt(s.left, s.minLeft), s.maxLeft), s.oldTop = s.top = wt(xt(s.top, s.minTop), s.maxTop), this.$canvas.css({
                width: s.width,
                height: s.height,
                left: s.left,
                top: s.top
            }), this.renderImage(), this.isCropped && this.isLimited && this.limitCropBox(!0, !0), t && this.output()
        }, renderImage: function (i) {
            var e, s = this.canvas, a = this.image;
            a.rotate && (e = l({
                width: s.width,
                height: s.height,
                degree: a.rotate,
                aspectRatio: a.aspectRatio
            }, !0)), t.extend(a, e ? {
                width: e.width,
                height: e.height,
                left: (s.width - e.width) / 2,
                top: (s.height - e.height) / 2
            } : {width: s.width, height: s.height, left: 0, top: 0}), this.$clone.css({
                width: a.width,
                height: a.height,
                marginLeft: a.left,
                marginTop: a.top,
                transform: p(a)
            }), i && this.output()
        }, initCropBox: function () {
            var i = this.options, e = this.canvas, s = i.aspectRatio, a = vt(i.autoCropArea) || .8, o = {
                width: e.width,
                height: e.height
            };
            s && (e.height * s > e.width ? o.height = o.width / s : o.width = o.height * s), this.cropBox = o, this.limitCropBox(!0, !0), o.width = wt(xt(o.width, o.minWidth), o.maxWidth), o.height = wt(xt(o.height, o.minHeight), o.maxHeight), o.width = xt(o.minWidth, o.width * a), o.height = xt(o.minHeight, o.height * a), o.oldLeft = o.left = e.left + (e.width - o.width) / 2, o.oldTop = o.top = e.top + (e.height - o.height) / 2, this.initialCropBox = t.extend({}, o)
        }, limitCropBox: function (t, i) {
            var e, s, a, o, h = this.options, n = h.aspectRatio, r = this.container, p = r.width, l = r.height, c = this.canvas, d = this.cropBox, g = this.isLimited;
            t && (e = vt(h.minCropBoxWidth) || 0, s = vt(h.minCropBoxHeight) || 0, e = wt(e, p), s = wt(s, l), a = wt(p, g ? c.width : p), o = wt(l, g ? c.height : l), n && (e && s ? s * n > e ? s = e / n : e = s * n : e ? s = e / n : s && (e = s * n), o * n > a ? o = a / n : a = o * n), d.minWidth = wt(e, a), d.minHeight = wt(s, o), d.maxWidth = a, d.maxHeight = o), i && (g ? (d.minLeft = xt(0, c.left), d.minTop = xt(0, c.top), d.maxLeft = wt(p, c.left + c.width) - d.width, d.maxTop = wt(l, c.top + c.height) - d.height) : (d.minLeft = 0, d.minTop = 0, d.maxLeft = p - d.width, d.maxTop = l - d.height))
        }, renderCropBox: function () {
            var t = this.options, i = this.container, e = i.width, s = i.height, a = this.cropBox;
            (a.width > a.maxWidth || a.width < a.minWidth) && (a.left = a.oldLeft), (a.height > a.maxHeight || a.height < a.minHeight) && (a.top = a.oldTop), a.width = wt(xt(a.width, a.minWidth), a.maxWidth), a.height = wt(xt(a.height, a.minHeight), a.maxHeight), this.limitCropBox(!1, !0), a.oldLeft = a.left = wt(xt(a.left, a.minLeft), a.maxLeft), a.oldTop = a.top = wt(xt(a.top, a.minTop), a.maxTop), t.movable && t.cropBoxMovable && this.$face.data(it, a.width === e && a.height === s ? dt : lt), this.$cropBox.css({
                width: a.width,
                height: a.height,
                left: a.left,
                top: a.top
            }), this.isCropped && this.isLimited && this.limitCanvas(!0, !0), this.isDisabled || this.output()
        }, output: function () {
            this.preview(), this.isCompleted ? this.trigger(Z, this.getData()) : this.isBuilt || this.$element.one(S, t.proxy(function () {
                this.trigger(Z, this.getData())
            }, this))
        }, initPreview: function () {
            var i, e = n(this.crossOrigin), s = e ? this.crossOriginUrl : this.url;
            this.$preview = t(this.options.preview), this.$clone2 = i = t("<img" + e + ' src="' + s + '">'), this.$viewBox.html(i), this.$preview.each(function () {
                var i = t(this);
                i.data(tt, {
                    width: i.width(),
                    height: i.height(),
                    html: i.html()
                }), i.html("<img" + e + ' src="' + s + '" style="display:block;width:100%;height:auto;min-width:0!important;min-height:0!important;max-width:none!important;max-height:none!important;image-orientation:0deg!important;">')
            })
        }, resetPreview: function () {
            this.$preview.each(function () {
                var i = t(this), e = i.data(tt);
                i.css({width: e.width, height: e.height}).html(e.html).removeData(tt)
            })
        }, preview: function () {
            var i = this.image, e = this.canvas, s = this.cropBox, a = s.width, o = s.height, h = i.width, n = i.height, r = s.left - e.left - i.left, l = s.top - e.top - i.top;
            this.isCropped && !this.isDisabled && (this.$clone2.css({
                width: h,
                height: n,
                marginLeft: -r,
                marginTop: -l,
                transform: p(i)
            }), this.$preview.each(function () {
                var e = t(this), s = e.data(tt), c = s.width, d = s.height, g = c, u = d, f = 1;
                a && (f = c / a, u = o * f), o && u > d && (f = d / o, g = a * f, u = d), e.css({
                    width: g,
                    height: u
                }).find("img").css({
                    width: h * f,
                    height: n * f,
                    marginLeft: -r * f,
                    marginTop: -l * f,
                    transform: p(i)
                })
            }))
        }, bind: function () {
            var i = this.options, e = this.$element, s = this.$cropper;
            t.isFunction(i.cropstart) && e.on(N, i.cropstart), t.isFunction(i.cropmove) && e.on(_, i.cropmove), t.isFunction(i.cropend) && e.on(q, i.cropend), t.isFunction(i.crop) && e.on(Z, i.crop), t.isFunction(i.zoom) && e.on(K, i.zoom), s.on(z, t.proxy(this.cropStart, this)), i.zoomable && i.zoomOnWheel && s.on(P, t.proxy(this.wheel, this)), i.toggleDragModeOnDblclick && s.on(U, t.proxy(this.dblclick, this)), x.on(O, this._cropMove = a(this.cropMove, this)).on(E, this._cropEnd = a(this.cropEnd, this)), i.responsive && w.on(j, this._resize = a(this.resize, this))
        }, unbind: function () {
            var i = this.options, e = this.$element, s = this.$cropper;
            t.isFunction(i.cropstart) && e.off(N, i.cropstart), t.isFunction(i.cropmove) && e.off(_, i.cropmove), t.isFunction(i.cropend) && e.off(q, i.cropend), t.isFunction(i.crop) && e.off(Z, i.crop), t.isFunction(i.zoom) && e.off(K, i.zoom), s.off(z, this.cropStart), i.zoomable && i.zoomOnWheel && s.off(P, this.wheel), i.toggleDragModeOnDblclick && s.off(U, this.dblclick), x.off(O, this._cropMove).off(E, this._cropEnd), i.responsive && w.off(j, this._resize)
        }, resize: function () {
            var i, e, s, a = this.options.restore, o = this.$container, h = this.container;
            !this.isDisabled && h && (s = o.width() / h.width, (1 !== s || o.height() !== h.height) && (a && (i = this.getCanvasData(), e = this.getCropBoxData()), this.render(), a && (this.setCanvasData(t.each(i, function (t, e) {
                i[t] = e * s
            })), this.setCropBoxData(t.each(e, function (t, i) {
                e[t] = i * s
            })))))
        }, dblclick: function () {
            this.isDisabled || (this.$dragBox.hasClass(W) ? this.setDragMode(dt) : this.setDragMode(ct))
        }, wheel: function (i) {
            var e = i.originalEvent || i, s = vt(this.options.wheelZoomRatio) || .1, a = 1;
            this.isDisabled || (i.preventDefault(), this.wheeling || (this.wheeling = !0, setTimeout(t.proxy(function () {
                this.wheeling = !1
            }, this), 50), e.deltaY ? a = e.deltaY > 0 ? 1 : -1 : e.wheelDelta ? a = -e.wheelDelta / 120 : e.detail && (a = e.detail > 0 ? 1 : -1), this.zoom(-a * s, i)))
        }, cropStart: function (i) {
            var e, s, a = this.options, o = i.originalEvent, h = o && o.touches, n = i;
            if (!this.isDisabled) {
                if (h) {
                    if (e = h.length, e > 1) {
                        if (!a.zoomable || !a.zoomOnTouch || 2 !== e)return;
                        n = h[1], this.startX2 = n.pageX, this.startY2 = n.pageY, s = gt
                    }
                    n = h[0]
                }
                if (s = s || t(n.target).data(it), Q.test(s)) {
                    if (this.trigger(N, {originalEvent: o, action: s}).isDefaultPrevented())return;
                    i.preventDefault(), this.action = s, this.cropping = !1, this.startX = n.pageX || o && o.pageX, this.startY = n.pageY || o && o.pageY, s === ct && (this.cropping = !0, this.$dragBox.addClass(T))
                }
            }
        }, cropMove: function (t) {
            var i, e = this.options, s = t.originalEvent, a = s && s.touches, o = t, h = this.action;
            if (!this.isDisabled) {
                if (a) {
                    if (i = a.length, i > 1) {
                        if (!e.zoomable || !e.zoomOnTouch || 2 !== i)return;
                        o = a[1], this.endX2 = o.pageX, this.endY2 = o.pageY
                    }
                    o = a[0]
                }
                if (h) {
                    if (this.trigger(_, {originalEvent: s, action: h}).isDefaultPrevented())return;
                    t.preventDefault(), this.endX = o.pageX || s && s.pageX, this.endY = o.pageY || s && s.pageY, this.change(o.shiftKey, h === gt ? t : null)
                }
            }
        }, cropEnd: function (t) {
            var i = t.originalEvent, e = this.action;
            this.isDisabled || e && (t.preventDefault(), this.cropping && (this.cropping = !1, this.$dragBox.toggleClass(T, this.isCropped && this.options.modal)), this.action = "", this.trigger(q, {
                originalEvent: i,
                action: e
            }))
        }, change: function (t, i) {
            var e, s, a = this.options, o = a.aspectRatio, h = this.action, n = this.container, r = this.canvas, p = this.cropBox, l = p.width, c = p.height, d = p.left, g = p.top, u = d + l, f = g + c, m = 0, v = 0, w = n.width, x = n.height, C = !0;
            switch (!o && t && (o = l && c ? l / c : 1), this.limited && (m = p.minLeft, v = p.minTop, w = m + wt(n.width, r.left + r.width), x = v + wt(n.height, r.top + r.height)), s = {
                x: this.endX - this.startX,
                y: this.endY - this.startY
            }, o && (s.X = s.y * o, s.Y = s.x / o), h) {
                case lt:
                    d += s.x, g += s.y;
                    break;
                case et:
                    if (s.x >= 0 && (u >= w || o && (v >= g || f >= x))) {
                        C = !1;
                        break
                    }
                    l += s.x, o && (c = l / o, g -= s.Y / 2), 0 > l && (h = st, l = 0);
                    break;
                case ot:
                    if (s.y <= 0 && (v >= g || o && (m >= d || u >= w))) {
                        C = !1;
                        break
                    }
                    c -= s.y, g += s.y, o && (l = c * o, d += s.X / 2), 0 > c && (h = at, c = 0);
                    break;
                case st:
                    if (s.x <= 0 && (m >= d || o && (v >= g || f >= x))) {
                        C = !1;
                        break
                    }
                    l -= s.x, d += s.x, o && (c = l / o, g += s.Y / 2), 0 > l && (h = et, l = 0);
                    break;
                case at:
                    if (s.y >= 0 && (f >= x || o && (m >= d || u >= w))) {
                        C = !1;
                        break
                    }
                    c += s.y, o && (l = c * o, d -= s.X / 2), 0 > c && (h = ot, c = 0);
                    break;
                case rt:
                    if (o) {
                        if (s.y <= 0 && (v >= g || u >= w)) {
                            C = !1;
                            break
                        }
                        c -= s.y, g += s.y, l = c * o
                    } else s.x >= 0 ? w > u ? l += s.x : s.y <= 0 && v >= g && (C = !1) : l += s.x, s.y <= 0 ? g > v && (c -= s.y, g += s.y) : (c -= s.y, g += s.y);
                    0 > l && 0 > c ? (h = nt, c = 0, l = 0) : 0 > l ? (h = pt, l = 0) : 0 > c && (h = ht, c = 0);
                    break;
                case pt:
                    if (o) {
                        if (s.y <= 0 && (v >= g || m >= d)) {
                            C = !1;
                            break
                        }
                        c -= s.y, g += s.y, l = c * o, d += s.X
                    } else s.x <= 0 ? d > m ? (l -= s.x, d += s.x) : s.y <= 0 && v >= g && (C = !1) : (l -= s.x, d += s.x), s.y <= 0 ? g > v && (c -= s.y, g += s.y) : (c -= s.y, g += s.y);
                    0 > l && 0 > c ? (h = ht, c = 0, l = 0) : 0 > l ? (h = rt, l = 0) : 0 > c && (h = nt, c = 0);
                    break;
                case nt:
                    if (o) {
                        if (s.x <= 0 && (m >= d || f >= x)) {
                            C = !1;
                            break
                        }
                        l -= s.x, d += s.x, c = l / o
                    } else s.x <= 0 ? d > m ? (l -= s.x, d += s.x) : s.y >= 0 && f >= x && (C = !1) : (l -= s.x, d += s.x), s.y >= 0 ? x > f && (c += s.y) : c += s.y;
                    0 > l && 0 > c ? (h = rt, c = 0, l = 0) : 0 > l ? (h = ht, l = 0) : 0 > c && (h = pt, c = 0);
                    break;
                case ht:
                    if (o) {
                        if (s.x >= 0 && (u >= w || f >= x)) {
                            C = !1;
                            break
                        }
                        l += s.x, c = l / o
                    } else s.x >= 0 ? w > u ? l += s.x : s.y >= 0 && f >= x && (C = !1) : l += s.x, s.y >= 0 ? x > f && (c += s.y) : c += s.y;
                    0 > l && 0 > c ? (h = pt, c = 0, l = 0) : 0 > l ? (h = nt, l = 0) : 0 > c && (h = rt, c = 0);
                    break;
                case dt:
                    this.move(s.x, s.y), C = !1;
                    break;
                case gt:
                    this.zoom(function (t, i, e, s) {
                        var a = yt(t * t + i * i), o = yt(e * e + s * s);
                        return (o - a) / a
                    }(Ct(this.startX - this.startX2), Ct(this.startY - this.startY2), Ct(this.endX - this.endX2), Ct(this.endY - this.endY2)), i), this.startX2 = this.endX2, this.startY2 = this.endY2, C = !1;
                    break;
                case ct:
                    if (!s.x || !s.y) {
                        C = !1;
                        break
                    }
                    e = this.$cropper.offset(), d = this.startX - e.left, g = this.startY - e.top, l = p.minWidth, c = p.minHeight, s.x > 0 ? h = s.y > 0 ? ht : rt : s.x < 0 && (d -= l, h = s.y > 0 ? nt : pt), s.y < 0 && (g -= c), this.isCropped || (this.$cropBox.removeClass(Y), this.isCropped = !0, this.limited && this.limitCropBox(!0, !0))
            }
            C && (p.width = l, p.height = c, p.left = d, p.top = g, this.action = h, this.renderCropBox()), this.startX = this.endX, this.startY = this.endY
        }, crop: function () {
            this.isBuilt && !this.isDisabled && (this.isCropped || (this.isCropped = !0, this.limitCropBox(!0, !0), this.options.modal && this.$dragBox.addClass(T), this.$cropBox.removeClass(Y)), this.setCropBoxData(this.initialCropBox))
        }, reset: function () {
            this.isBuilt && !this.isDisabled && (this.image = t.extend({}, this.initialImage), this.canvas = t.extend({}, this.initialCanvas), this.cropBox = t.extend({}, this.initialCropBox), this.renderCanvas(), this.isCropped && this.renderCropBox())
        }, clear: function () {
            this.isCropped && !this.isDisabled && (t.extend(this.cropBox, {
                left: 0,
                top: 0,
                width: 0,
                height: 0
            }), this.isCropped = !1, this.renderCropBox(), this.limitCanvas(!0, !0), this.renderCanvas(), this.$dragBox.removeClass(T), this.$cropBox.addClass(Y))
        }, replace: function (t, i) {
            !this.isDisabled && t && (this.isImg && this.$element.attr("src", t), i ? (this.url = t, this.$clone.attr("src", t), this.isBuilt && this.$preview.find("img").add(this.$clone2).attr("src", t)) : (this.isImg && (this.isReplaced = !0), this.options.data = null, this.load(t)))
        }, enable: function () {
            this.isBuilt && (this.isDisabled = !1, this.$cropper.removeClass(H))
        }, disable: function () {
            this.isBuilt && (this.isDisabled = !0, this.$cropper.addClass(H))
        }, destroy: function () {
            var t = this.$element;
            this.isLoaded ? (this.isImg && this.isReplaced && t.attr("src", this.originalUrl), this.unbuild(), t.removeClass(Y)) : this.isImg ? t.off(I, this.start) : this.$clone && this.$clone.remove(), t.removeData(L)
        }, move: function (t, i) {
            var s = this.canvas;
            this.moveTo(e(t) ? t : s.left + vt(t), e(i) ? i : s.top + vt(i))
        }, moveTo: function (t, s) {
            var a = this.canvas, o = !1;
            e(s) && (s = t), t = vt(t), s = vt(s), this.isBuilt && !this.isDisabled && this.options.movable && (i(t) && (a.left = t, o = !0), i(s) && (a.top = s, o = !0), o && this.renderCanvas(!0))
        }, zoom: function (t, i) {
            var e = this.canvas;
            t = vt(t), t = 0 > t ? 1 / (1 - t) : 1 + t, this.zoomTo(e.width * t / e.naturalWidth, i)
        }, zoomTo: function (t, i) {
            var e, s, a, o, h, n = this.options, r = this.canvas, p = r.width, l = r.height, c = r.naturalWidth, g = r.naturalHeight;
            if (t = vt(t), t >= 0 && this.isBuilt && !this.isDisabled && n.zoomable) {
                if (s = c * t, a = g * t, i && (e = i.originalEvent), this.trigger(K, {
                        originalEvent: e,
                        oldRatio: p / c,
                        ratio: s / c
                    }).isDefaultPrevented())return;
                e ? (o = this.$cropper.offset(), h = e.touches ? d(e.touches) : {
                    pageX: i.pageX || e.pageX || 0,
                    pageY: i.pageY || e.pageY || 0
                }, r.left -= (s - p) * ((h.pageX - o.left - r.left) / p), r.top -= (a - l) * ((h.pageY - o.top - r.top) / l)) : (r.left -= (s - p) / 2, r.top -= (a - l) / 2), r.width = s, r.height = a, this.renderCanvas(!0)
            }
        }, rotate: function (t) {
            this.rotateTo((this.image.rotate || 0) + vt(t))
        }, rotateTo: function (t) {
            t = vt(t), i(t) && this.isBuilt && !this.isDisabled && this.options.rotatable && (this.image.rotate = t % 360, this.isRotated = !0, this.renderCanvas(!0))
        }, scale: function (t, s) {
            var a = this.image, o = !1;
            e(s) && (s = t), t = vt(t), s = vt(s), this.isBuilt && !this.isDisabled && this.options.scalable && (i(t) && (a.scaleX = t, o = !0), i(s) && (a.scaleY = s, o = !0), o && this.renderImage(!0))
        }, scaleX: function (t) {
            var e = this.image.scaleY;
            this.scale(t, i(e) ? e : 1)
        }, scaleY: function (t) {
            var e = this.image.scaleX;
            this.scale(i(e) ? e : 1, t)
        }, getData: function (i) {
            var e, s, a = this.options, o = this.image, h = this.canvas, n = this.cropBox;
            return this.isBuilt && this.isCropped ? (s = {
                x: n.left - h.left,
                y: n.top - h.top,
                width: n.width,
                height: n.height
            }, e = o.width / o.naturalWidth, t.each(s, function (t, a) {
                a /= e, s[t] = i ? Dt(a) : a
            })) : s = {
                x: 0,
                y: 0,
                width: 0,
                height: 0
            }, a.rotatable && (s.rotate = o.rotate || 0), a.scalable && (s.scaleX = o.scaleX || 1, s.scaleY = o.scaleY || 1), s
        }, setData: function (e) {
            var s, a, o, h = this.options, n = this.image, r = this.canvas, p = {};
            t.isFunction(e) && (e = e.call(this.element)), this.isBuilt && !this.isDisabled && t.isPlainObject(e) && (h.rotatable && i(e.rotate) && e.rotate !== n.rotate && (n.rotate = e.rotate, this.isRotated = s = !0), h.scalable && (i(e.scaleX) && e.scaleX !== n.scaleX && (n.scaleX = e.scaleX, a = !0), i(e.scaleY) && e.scaleY !== n.scaleY && (n.scaleY = e.scaleY, a = !0)), s ? this.renderCanvas() : a && this.renderImage(), o = n.width / n.naturalWidth, i(e.x) && (p.left = e.x * o + r.left), i(e.y) && (p.top = e.y * o + r.top), i(e.width) && (p.width = e.width * o), i(e.height) && (p.height = e.height * o), this.setCropBoxData(p))
        }, getContainerData: function () {
            return this.isBuilt ? this.container : {}
        }, getImageData: function () {
            return this.isLoaded ? this.image : {}
        }, getCanvasData: function () {
            var i = this.canvas, e = {};
            return this.isBuilt && t.each(["left", "top", "width", "height", "naturalWidth", "naturalHeight"], function (t, s) {
                e[s] = i[s]
            }), e
        }, setCanvasData: function (e) {
            var s = this.canvas, a = s.aspectRatio;
            t.isFunction(e) && (e = e.call(this.$element)), this.isBuilt && !this.isDisabled && t.isPlainObject(e) && (i(e.left) && (s.left = e.left), i(e.top) && (s.top = e.top), i(e.width) ? (s.width = e.width, s.height = e.width / a) : i(e.height) && (s.height = e.height, s.width = e.height * a), this.renderCanvas(!0))
        }, getCropBoxData: function () {
            var t, i = this.cropBox;
            return this.isBuilt && this.isCropped && (t = {
                left: i.left,
                top: i.top,
                width: i.width,
                height: i.height
            }), t || {}
        }, setCropBoxData: function (e) {
            var s, a, o = this.cropBox, h = this.options.aspectRatio;
            t.isFunction(e) && (e = e.call(this.$element)), this.isBuilt && this.isCropped && !this.isDisabled && t.isPlainObject(e) && (i(e.left) && (o.left = e.left), i(e.top) && (o.top = e.top), i(e.width) && (s = !0, o.width = e.width), i(e.height) && (a = !0, o.height = e.height), h && (s ? o.height = o.width / h : a && (o.width = o.height * h)), this.renderCropBox())
        }, getCroppedCanvas: function (i) {
            var e, s, a, o, h, n, r, p, l, d, g;
            return this.isBuilt && this.isCropped && ft ? (t.isPlainObject(i) || (i = {}), g = this.getData(), e = g.width, s = g.height, p = e / s, t.isPlainObject(i) && (h = i.width, n = i.height, h ? (n = h / p, r = h / e) : n && (h = n * p, r = n / s)), a = $t(h || e), o = $t(n || s), l = t("<canvas>")[0], l.width = a, l.height = o, d = l.getContext("2d"), i.fillColor && (d.fillStyle = i.fillColor, d.fillRect(0, 0, a, o)), d.drawImage.apply(d, function () {
                var t, i, a, o, h, n, p = c(this.$clone[0], this.image), l = p.width, d = p.height, u = this.canvas, f = [p], m = g.x + u.naturalWidth * (Ct(g.scaleX || 1) - 1) / 2, v = g.y + u.naturalHeight * (Ct(g.scaleY || 1) - 1) / 2;
                return -e >= m || m > l ? m = t = a = h = 0 : 0 >= m ? (a = -m, m = 0, t = h = wt(l, e + m)) : l >= m && (a = 0, t = h = wt(e, l - m)), 0 >= t || -s >= v || v > d ? v = i = o = n = 0 : 0 >= v ? (o = -v, v = 0, i = n = wt(d, s + v)) : d >= v && (o = 0, i = n = wt(s, d - v)), f.push($t(m), $t(v), $t(t), $t(i)), r && (a *= r, o *= r, h *= r, n *= r), h > 0 && n > 0 && f.push($t(a), $t(o), $t(h), $t(n)), f
            }.call(this)), l) : void 0
        }, setAspectRatio: function (t) {
            var i = this.options;
            this.isDisabled || e(t) || (i.aspectRatio = xt(0, t) || NaN, this.isBuilt && (this.initCropBox(), this.isCropped && this.renderCropBox()))
        }, setDragMode: function (t) {
            var i, e, s = this.options;
            this.isLoaded && !this.isDisabled && (i = t === ct, e = s.movable && t === dt, t = i || e ? t : ut, this.$dragBox.data(it, t).toggleClass(W, i).toggleClass(M, e), s.cropBoxMovable || this.$face.data(it, t).toggleClass(W, i).toggleClass(M, e))
        }
    }, v.DEFAULTS = {
        viewMode: 0,
        dragMode: "crop",
        aspectRatio: NaN,
        data: null,
        preview: "",
        responsive: !0,
        restore: !0,
        checkCrossOrigin: !0,
        checkOrientation: !0,
        modal: !0,
        guides: !0,
        center: !0,
        highlight: !0,
        background: !0,
        autoCrop: !0,
        autoCropArea: .8,
        movable: !0,
        rotatable: !0,
        scalable: !0,
        zoomable: !0,
        zoomOnTouch: !0,
        zoomOnWheel: !0,
        wheelZoomRatio: .1,
        cropBoxMovable: !0,
        cropBoxResizable: !0,
        toggleDragModeOnDblclick: !0,
        minCanvasWidth: 0,
        minCanvasHeight: 0,
        minCropBoxWidth: 0,
        minCropBoxHeight: 0,
        minContainerWidth: 200,
        minContainerHeight: 100,
        build: null,
        built: null,
        cropstart: null,
        cropmove: null,
        cropend: null,
        crop: null,
        zoom: null
    }, v.setDefaults = function (i) {
        t.extend(v.DEFAULTS, i)
    }, v.TEMPLATE = '<div class="cropper-container"><div class="cropper-wrap-box"><div class="cropper-canvas"></div></div><div class="cropper-drag-box"></div><div class="cropper-crop-box"><span class="cropper-view-box"></span><span class="cropper-dashed dashed-h"></span><span class="cropper-dashed dashed-v"></span><span class="cropper-center"></span><span class="cropper-face"></span><span class="cropper-line line-e" data-action="e"></span><span class="cropper-line line-n" data-action="n"></span><span class="cropper-line line-w" data-action="w"></span><span class="cropper-line line-s" data-action="s"></span><span class="cropper-point point-e" data-action="e"></span><span class="cropper-point point-n" data-action="n"></span><span class="cropper-point point-w" data-action="w"></span><span class="cropper-point point-s" data-action="s"></span><span class="cropper-point point-ne" data-action="ne"></span><span class="cropper-point point-nw" data-action="nw"></span><span class="cropper-point point-sw" data-action="sw"></span><span class="cropper-point point-se" data-action="se"></span></div></div>', v.other = t.fn.cropper, t.fn.cropper = function (i) {
        var a, o = s(arguments, 1);
        return this.each(function () {
            var e, s, h = t(this), n = h.data(L);
            if (!n) {
                if (/destroy/.test(i))return;
                e = t.extend({}, h.data(), t.isPlainObject(i) && i), h.data(L, n = new v(this, e))
            }
            "string" == typeof i && t.isFunction(s = n[i]) && (a = s.apply(n, o))
        }), e(a) ? this : a
    }, t.fn.cropper.Constructor = v, t.fn.cropper.setDefaults = v.setDefaults, t.fn.cropper.noConflict = function () {
        return t.fn.cropper = v.other, this
    }
});