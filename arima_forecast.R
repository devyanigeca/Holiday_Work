data = read.csv('C:/Users/Admin/Desktop/SIH_2019/datasets/Tractor-Sales.csv')
data = ts(data[,2],start = c(2003,1),frequency = 4)
plot(data, xlab='Years', ylab = 'Tractor Sales')

plot(diff(data),ylab='Differenced Tractor Sales')

plot(log10(data),ylab='Log (Tractor Sales)')


plot(diff(log10(data)),ylab='Differenced Log (Tractor Sales)')

par(mfrow = c(1,2))
acf(ts(diff(log10(data))),main='ACF Tractor Sales')
pacf(ts(diff(log10(data))),main='PACF Tractor Sales')

require(forecast)
ARIMAfit = auto.arima(log10(data), approximation=FALSE,trace=FALSE)
summary(ARIMAfit)

par(mfrow = c(1,1))
pred = predict(ARIMAfit, n.ahead = 36)
pred
plot(data,type='l',xlim=c(2004,2018),ylim=c(1,1600),xlab = 'Year',ylab = 'Tractor Sales')
lines(10^(pred$pred),col='blue')
lines(10^(pred$pred+2*pred$se),col='orange')
lines(10^(pred$pred-2*pred$se),col='orange')


par(mfrow=c(1,2))
acf(ts(ARIMAfit$residuals),main='ACF Residual')
pacf(ts(ARIMAfit$residuals),main='PACF Residual')
