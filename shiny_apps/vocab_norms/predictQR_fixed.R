predictQR_fixed <- function (object, newdata, xreg) 
{
  bspline <- function(x, ndx, xlr = NULL, knots = NULL, deg = 3, 
                      deriv = 0, outer.ok = FALSE) {
    if (is.null(knots)) {
      if (is.null(xlr)) {
        xl <- min(x) - 0.01 * diff(range(x))
        xr <- max(x) + 0.01 * diff(range(x))
      }
      else {
        if (length(xlr) != 2) 
          stop("quando fornito, xlr deve avere due componenti")
        xl <- xlr[1]
        xr <- xlr[2]
      }
      dx <- (xr - xl)/ndx
      knots <- seq(xl - deg * dx, xr + deg * dx, by = dx)
    }
    B <- splineDesign(knots, x, ord = deg + 1, derivs = rep(deriv, 
                                                            length(x)), outer.ok = outer.ok)
    B
  }
  b <- as.matrix(object$coefficients)
  if (missing(xreg)) {
    if (missing(newdata)) 
      stop("please, provide `newdata' or 'xreg'")
    nomiCoef <- rownames(b)
    info.smooth <- object$info.smooth
    p <- info.smooth$deg + info.smooth$ndx
    nome.smooth <- names(object$BB)
    nomiCoefPen <- paste(nome.smooth, ".ps.", 1:p, sep = "")
    id.coef.smooth <- match(nomiCoefPen, nomiCoef)
    b.smooth <- b[id.coef.smooth, ]
    nomiCoefUnpen <- nomiCoef[-id.coef.smooth]
    nomiVarModello <- all.vars(object$call$formula)[-1]
    id.var <- match(nomiVarModello, names(newdata))
    if (any(is.na(id.var))) 
      stop("`newdata' does not include all the covariates in the model")
    newdata <- newdata[, id.var, drop = FALSE]
    x.new <- newdata[, match(nome.smooth, names(newdata))]
    newdata <- newdata[, -match(nome.smooth, names(newdata)), 
                       drop = FALSE]
    m <- min(attr(object$BB[[1]], "covariate.35"))
    M <- max(attr(object$BB[[1]], "covariate.35"))
    B.new <- bspline(c(m, x.new, M), ndx = info.smooth$ndx, 
                     deg = info.smooth$deg)
    B.new <- B.new[-c(1, nrow(B.new)), ]
    XREG <- as.matrix(cbind(newdata, B.new))
    colnames(XREG) <- c(nomiCoefUnpen, nomiCoefPen)
    if ("(Intercept)" %in% nomiCoef) 
      XREG <- cbind(`(Intercept)` = 1, XREG)
    fit <- drop(XREG[, nomiCoef] %*% b)
  }
  else {
    if (!missing(newdata)) 
      warning("`newdata' ignored when 'xreg' is provided")
    fit <- drop(xreg %*% b)
  }
  return(fit)
}