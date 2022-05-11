library(ggplot2)
gpl<- ggplot(df, aes(x = avg_glucose_level, y = age,color=age)) +
  geom_point() +
  labs(x = "Average glucose level", y = "Age", color = "Age:")+
  scale_x_continuous(breaks = round(seq(10, 300, by = 50),0)) + scale_y_continuous(breaks = round(seq(10, 300, by = 50),0))
  gpl + scale_color_continuous()

 plot1 <- gpl + scale_color_viridis_c() + ggtitle("'magma' (default)")
 plot2 <- gpl + scale_colour_viridis_c(option = "inferno") + ggtitle("'inferno'")
 plot3 <- gpl + scale_colour_viridis_c(option = "plasma") + ggtitle("'plasma'")
 plot4 <- gpl + scale_colour_viridis_c(option = "cividis") + ggtitle("'rocket'")

library(patchwork)
(plot1 + plot2 + plot3 + plot4) * theme(legend.position = "bottom")

 