install.packages("ggridges")

library(ggridges)

library(ggplot2)

ggplot(df, aes(x = age, y = work_type, fill = work_type)) +
  geom_density_ridges() +  
  theme_ridges() + 
  theme(legend.position = "none")+
  ggtitle("Ridgeline plot working type by age ") +
  xlab("Age") + ylab("Working status")+
  theme(plot.title = element_text(hjust = 0.5), panel.background = element_blank())

